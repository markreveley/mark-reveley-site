#!/usr/bin/env python3
"""Render a discussion YAML record as a readable Markdown transcript."""

import argparse
import os
from pathlib import Path

import yaml


def render(source, record, output):
    if record.get("schema_version") != 1 or record.get("kind") != "discussion":
        raise ValueError("Expected a version 1 discussion record")
    entries = [record["post"], *record["comments"]]
    ids = [entry["id"] for entry in entries]
    if ids[0] != "post" or len(ids) != len(set(ids)):
        raise ValueError("The post must have ID 'post'; all entry IDs must be unique")
    for entry in entries:
        if entry["content_status"] not in {"present", "not_in_capture"}:
            raise ValueError(f"Unknown content status: {entry['id']}")
        if not isinstance(entry["body"], str):
            raise ValueError(f"Body must be text: {entry['id']}")
        if bool(entry["body"].strip()) != (entry["content_status"] == "present"):
            raise ValueError(f"Body and content status disagree: {entry['id']}")
    for entry in record["comments"]:
        parent = entry["parent_id"]
        basis = entry["parent_basis"]
        if basis not in {"explicit", "inferred", "unknown"}:
            raise ValueError(f"Unknown parent basis: {entry['id']}")
        if (parent is None) != (basis == "unknown"):
            raise ValueError(f"Parent and basis disagree: {entry['id']}")
        if parent is not None and (parent not in ids or parent == entry["id"]):
            raise ValueError(f"Invalid parent for {entry['id']}: {parent}")

    relative_source = Path(os.path.relpath(source, output.parent)).as_posix()
    relative_renderer = Path(
        os.path.relpath(Path(__file__).resolve(), output.parent)
    ).as_posix()
    lines = [
        f"# {record['title']}", "",
        f"Source: [{record['platform']} discussion]({record['url']})", "",
        f"Structured record: [{record['id']}]({relative_source}). "
        f"Generated with [render_discussion.py]({relative_renderer}); "
        "edit the YAML record.", "",
    ]
    capture = record["capture"]
    if capture["raw_file"]:
        raw = source.parent / capture["raw_file"]
        relative_raw = Path(os.path.relpath(raw, output.parent)).as_posix()
        lines += [f"[Original capture]({relative_raw}).", ""]
    lines += [
        f"Capture: {capture['completeness']}; live verification: "
        f"{capture['live_verification']}. Relative ages and scores belong to the capture.", "",
        "Comments follow capture order. Unknown reply nesting is left unspecified; "
        "inferred relationships are labeled. Missing bodies are marked without "
        "assuming deletion. Post and comment bodies follow.", "",
    ]
    for index, entry in enumerate(entries):
        lines += [f"## {entry['id']}", ""]
        author = entry.get("author") or "Unknown author"
        label = "Post" if index == 0 else "Comment"
        metadata = [f"{label} by **{author}**"]
        if entry.get("author_is_op"):
            metadata.append("OP")
        if index == 0 and entry.get("author_basis") == "inferred_from_op_badge":
            metadata.append("author inferred from OP badges in comments")
        if entry.get("published_at"):
            metadata.append(f"published: {entry['published_at']}")
        if entry.get("age_label"):
            metadata.append(entry["age_label"])
        if entry.get("displayed_score") is not None:
            metadata.append(f"displayed score: {entry['displayed_score']}")
        if index and entry["parent_id"]:
            parent = entry["parent_id"]
            metadata.append(f"reply to [{parent}](#{parent}) ({entry['parent_basis']})")
        lines += [" · ".join(metadata), ""]
        if entry["content_status"] == "not_in_capture":
            lines += ["*No body was present in the supplied capture.*", ""]
        else:
            lines += entry["body"].splitlines()
            lines += [""]
        for note in entry.get("notes", []):
            lines += [f"Capture note: {note}", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error("Source and output must be different files")
    record = yaml.safe_load(args.source.read_text(encoding="utf-8"))
    result = render(args.source, record, args.output)
    args.output.write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
