(() => {
  "use strict";

  const quoteSlugs = ["2026-08-31-tests-independent-of-code", "2026-08-31-tests-as-risk-mitigation", "2026-08-31-test-purity-performance-stability", "2026-08-31-test-purity-and-extent", "2026-08-31-software-factory-infrastructure-not-teammate", "2026-08-31-sans-io-software-architecture", "2026-08-31-programming-as-theory-building", "2026-08-31-optimize-test-purity-not-extent", "2026-08-31-minimalist-zsh-setup", "2026-08-31-mastering-llms-is-mastering-malloc", "2026-08-31-losing-the-project-mental-model", "2026-08-31-llms-shift-judgment-to-artifact", "2026-08-31-ironies-of-classic-automation", "2026-08-31-human-taste-encoded-in-the-environment", "2026-08-31-gwt-requires-temporal-persistence", "2026-08-31-failing-test-cannot-be-negotiated", "2026-08-31-edge-case-patches-over-core-pathfinding", "2026-08-31-delete-cargo-integration-tests", "2026-08-31-data-driven-test-check-function", "2026-08-31-comprehension-debt-understanding-gap", "2026-08-31-cognitive-debt-origin-in-student-products", "2026-08-31-cognitive-debt-lives-in-developer-minds", "2026-08-31-coding-agents-supersede-human-code-review", "2026-08-31-cloud-software-factory-core-loop", "2026-08-31-ai-productivity-is-not-competence", "2026-08-31-ai-productivity-gains-stop-at-company-level", "2026-08-31-ai-creation-savings-shift-to-verification", "2026-08-31-ai-code-security-is-a-scale-problem", "2026-08-31-ai-code-review-walkthrough", "2026-08-31-ai-code-maintainability-signals-decline", "2026-08-31-agents-expose-the-infinite-backlog", "2026-08-30-verification-national-scale-engineering", "2026-08-30-unix-environment-agentic-harness", "2026-08-30-tests-confirm-the-wrong-thing", "2026-08-30-spec-is-product-thinking", "2026-08-30-principles-and-feedback-loops", "2026-08-30-infrastructure-for-agent-factories", "2026-08-30-feedback-requires-generalization", "2026-08-30-agents-run-tools-in-a-loop", "2026-08-30-agents-fill-requirement-gaps", "2026-08-30-agent-legible-design-systems", "2026-08-30-agent-instructions-reviewed-as-code", "2026-08-29-train-agents-md-on-real-sessions", "2026-08-29-saas-businesses-as-model-harnesses", "2026-08-29-rlhf-likable-humans-rlvr-accepted-machines", "2026-08-29-long-horizon-agents-against-human-in-loop", "2026-08-29-harness-manages-agent-world", "2026-08-29-flue-durable-agent-workflows", "2026-08-29-first-party-harness-baked-in", "2026-08-29-empathy-is-a-manufactured-quantity", "2026-08-29-commit-scope-is-most-important", "2026-08-29-cmdatom-compose-macros-on-the-fly", "2026-08-29-better-harnesses-help-weaker-models", "2026-08-29-agent-harness-saas-network-effects"];
  const button = document.querySelector("[data-random-quote]");
  if (!button || quoteSlugs.length === 0) return;

  const root = button.dataset.root || "";
  const filtersOn = button.dataset.filters === "on";
  const pageName = filtersOn ? "quotes-expanded.html" : "quotes.html";
  const parameters = new URLSearchParams(window.location.search);
  const requestedSlug = parameters.get("quote");
  const requestedFace = Number(parameters.get("die"));
  const hasRequestedFace = Number.isInteger(requestedFace)
    && requestedFace >= 1 && requestedFace <= 6;

  function showDieFace(value) {
    for (const face of button.querySelectorAll("[data-die-face]")) {
      face.classList.toggle("is-visible", face.dataset.dieFace === String(value));
    }
  }

  if (hasRequestedFace) showDieFace(requestedFace);

  function showAssociatedFilters(card) {
    if (!filtersOn) return;

    const tagList = document.querySelector(".filter-rail-tags ul");
    if (tagList) {
      const rows = Array.from(card.querySelectorAll(".tags a"), (link) => {
        const item = document.createElement("li");
        const associatedLink = link.cloneNode(true);
        associatedLink.setAttribute("aria-current", "page");
        item.append(associatedLink);
        return item;
      });
      tagList.replaceChildren(...rows);
    }

    const sourceList = document.querySelector(".filter-rail-sources ul");
    if (sourceList) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = card.dataset.sourceFilterHref;
      link.textContent = card.dataset.sourceFilter;
      link.setAttribute("aria-current", "page");
      item.append(link);
      sourceList.replaceChildren(item);
    }
  }

  if (requestedSlug) {
    const cards = Array.from(document.querySelectorAll(".card.quote"));
    const selectedCard = cards.find((card) => card.dataset.quoteSlug === requestedSlug);
    if (selectedCard) {
      for (const card of cards) card.hidden = card !== selectedCard;
      showAssociatedFilters(selectedCard);

      const eye = document.querySelector(".filter-toggle");
      if (eye) {
        const eyePage = filtersOn ? "quotes.html" : "quotes-expanded.html";
        const eyeParameters = new URLSearchParams({ quote: requestedSlug });
        if (hasRequestedFace) eyeParameters.set("die", String(requestedFace));
        eye.href = `${root}${eyePage}?${eyeParameters}`;
      }
    }
  }

  button.addEventListener("click", () => {
    const choices = quoteSlugs.length > 1
      ? quoteSlugs.filter((slug) => slug !== requestedSlug)
      : quoteSlugs;
    const chosen = choices[Math.floor(Math.random() * choices.length)];
    const rolledFace = Math.floor(Math.random() * 6) + 1;
    showDieFace(rolledFace);
    const nextParameters = new URLSearchParams({
      quote: chosen,
      die: String(rolledFace),
    });
    window.location.assign(`${root}${pageName}?${nextParameters}`);
  });
})();
