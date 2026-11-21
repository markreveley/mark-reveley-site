(() => {
  "use strict";

  const postSlugs = ["2026-11-20-the-devil-is-in-the-spec", "2026-11-13-the-governance-spiral", "2026-11-06-seek-confusion", "2026-10-30-artifacts-no-longer-have-inherent-value", "2026-10-24-llms-are-tools-maybe", "2026-10-16-propositions", "2026-09-25-letting-the-llm-drive-me", "2026-09-18-agent-failure-concept-document", "2026-09-09-the-llm-silo-paradox", "2026-09-03-complexity-escape", "arriving-has-utility"];
  const button = document.querySelector("[data-random-post]");
  if (!button) return;

  const root = button.dataset.root || "";
  const parameters = new URLSearchParams(window.location.search);
  const postBody = document.querySelector(".post-body[data-post-slug]");
  const currentSlug = postBody ? postBody.dataset.postSlug : parameters.get("post");
  const requestedFace = Number(parameters.get("die"));
  const hasRequestedFace = Number.isInteger(requestedFace)
    && requestedFace >= 1 && requestedFace <= 6;

  function showDieFace(value) {
    for (const face of button.querySelectorAll("[data-die-face]")) {
      face.classList.toggle("is-visible", face.dataset.dieFace === String(value));
    }
  }

  if (hasRequestedFace) showDieFace(requestedFace);

  // index.html?post=<slug> and index-expanded.html?post=<slug> show one post's
  // card; with the eye on, the tag rail lists only that post's tags.
  const requestedSlug = parameters.get("post");
  if (requestedSlug) {
    const cards = Array.from(document.querySelectorAll(".card.post"));
    const selectedCard = cards.find((card) => card.dataset.postSlug === requestedSlug);
    if (selectedCard) {
      for (const card of cards) card.hidden = card !== selectedCard;
      const tagList = document.querySelector(".filter-rail-tags ul");
      if (tagList) {
        const rows = Array.from(selectedCard.querySelectorAll(".tags a"), (link) => {
          const item = document.createElement("li");
          const tagLink = link.cloneNode(true);
          tagLink.setAttribute("aria-current", "page");
          item.append(tagLink);
          return item;
        });
        tagList.replaceChildren(...rows);
      }
    }
  }

  // Carry the shown post through the eye, so toggling keeps the same post.
  const eye = document.querySelector(".filter-toggle");
  if (eye && currentSlug && postSlugs.includes(currentSlug)) {
    const eyeUrl = new URL(eye.getAttribute("href"), window.location.href);
    eyeUrl.searchParams.set("post", currentSlug);
    if (hasRequestedFace) eyeUrl.searchParams.set("die", String(requestedFace));
    eye.href = eyeUrl.href;
  }

  if (postSlugs.length === 0) {
    button.disabled = true;
    return;
  }

  button.addEventListener("click", () => {
    const choices = postSlugs.length > 1
      ? postSlugs.filter((slug) => slug !== currentSlug)
      : postSlugs;
    const chosen = choices[Math.floor(Math.random() * choices.length)];
    const rolledFace = Math.floor(Math.random() * 6) + 1;
    showDieFace(rolledFace);
    const next = new URLSearchParams({ die: String(rolledFace) });
    window.location.assign(`${root}posts/${encodeURIComponent(chosen)}.html?${next}`);
  });
})();
