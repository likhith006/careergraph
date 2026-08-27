const searchInput = document.getElementById("career-search");
const suggestionsBox = document.getElementById("search-suggestions");

if (searchInput && suggestionsBox) {

    const careerCards =
        document.querySelectorAll(".career-card");

    searchInput.addEventListener("input", () => {

        const searchTerm =
            searchInput.value.toLowerCase().trim();

        suggestionsBox.innerHTML = "";

        careerCards.forEach(card => {

            const careerName =
                card.dataset.careerName;

            const careerNameLower =
                careerName.toLowerCase();

            // Filter cards
            if (
                searchTerm === "" ||
                careerNameLower.includes(searchTerm)
            ) {
                card.style.display = "";
            } else {
                card.style.display = "none";
            }

            // Create suggestions
            if (
                searchTerm !== "" &&
                careerNameLower.includes(searchTerm)
            ) {

                const suggestion =
                    document.createElement("a");

                suggestion.href = card.href;

                suggestion.className =
                    "search-suggestion";

                suggestion.textContent =
                    careerName;

                suggestionsBox.appendChild(
                    suggestion
                );
            }

        });

        // Show/hide suggestion box
        if (
            searchTerm !== "" &&
            suggestionsBox.children.length > 0
        ) {
            suggestionsBox.style.display = "block";
        } else {
            suggestionsBox.style.display = "none";
        }

    });

    // Hide suggestions when clicking outside
    document.addEventListener("click", (event) => {

        if (!event.target.closest(".search-box")) {
            suggestionsBox.style.display = "none";
        }

    });

}
document.addEventListener("DOMContentLoaded", async () => {

    const graphContainer = document.getElementById("career-graph");

    if (!graphContainer) {
        return;
    }

    const careerName = document.body.dataset.career;

    try {

        const response = await fetch(
            `/api/career/${encodeURIComponent(careerName)}/graph`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to load graph");
        }

        if (!data.length) {
            graphContainer.innerHTML =
                "<p>No graph data available.</p>";
            return;
        }

        const elements = [];

        const nodeIds = new Set();

        data.forEach(item => {

            // Source node
            if (!nodeIds.has(item.source_id)) {

                elements.push({
                    data: {
                        id: item.source_id,
                        label: item.source_name,
                        type: item.source_type
                    }
                });

                nodeIds.add(item.source_id);
            }

            // Target node
            if (item.target_id && !nodeIds.has(item.target_id)) {

                elements.push({
                    data: {
                        id: item.target_id,
                        label: item.target_name,
                        type: item.target_type
                    }
                });

                nodeIds.add(item.target_id);
            }

            // Relationship
            if (item.target_id && item.relationship) {

                elements.push({
                    data: {
                        id:
                            `${item.source_id}-${item.target_id}-${item.relationship}`,

                        source: item.source_id,

                        target: item.target_id,

                        label: item.relationship
                    }
                });
            }
        });


        const cy = cytoscape({

            container: graphContainer,

            elements: elements,

            style: [
                {
    selector: "node",

    style: {
        "label": "data(label)",
        "text-valign": "center",
        "text-halign": "center",
        "color": "#1d1d1f",
        "font-size": "12px",
        "width": "75px",
        "height": "75px",
        "border-width": 2,
        "border-color": "#1d1d1f",
        "background-color": "#eeeeea"
    }
},

{
    selector: 'node[type="Career"]',

    style: {
        "width": "110px",
        "height": "110px",
        "font-size": "14px",
        "font-weight": "bold"
    }
},

{
    selector: 'node[type="Skill"]',

    style: {
        "width": "80px",
        "height": "80px"
    }
},

{
    selector: 'node[type="Project"]',

    style: {
        "width": "90px",
        "height": "90px"
    }
}

               ,

                {
                    selector: "edge",

                    style: {
                        "width": 2,
                        "line-color": "#999",
                        "target-arrow-color": "#999",
                        "target-arrow-shape": "triangle",
                        "curve-style": "bezier",
                        "label": "data(label)",
                        "font-size": "9px",
                        "text-background-color": "#ffffff",
                        "text-background-opacity": 1,
                        "text-background-padding": "3px"
                    }
                }
            ],

            layout: {
                name: "cose",
                animate: true,
                padding: 40
            }
        });

    } catch (error) {

        console.error(error);

        graphContainer.innerHTML =
            `<p>Unable to load career graph: ${error.message}</p>`;
    }

});