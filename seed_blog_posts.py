from app import app, db
from models import BlogPost
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

# Sample blog posts data
sample_posts = [
    # Spring
    {
        "title": "Spring Garden Awakening: Essential Tasks for a Vibrant Start",
        "slug": "spring-garden-awakening",
        "summary": "Prepare your garden for the growing season with these essential spring tasks and planting ideas.",
        "content": """<p>As the frost thaws and the first signs of spring emerge, it's time to prepare your garden for the growing season ahead. This comprehensive guide covers all the essential tasks to ensure your garden awakens with vibrant energy.</p>

<h2>Spring Cleanup</h2>
<p>Before new growth begins, clear out winter debris, dead leaves, and fallen branches. Prune dead stems from perennials and ornamental grasses, but be careful not to damage emerging shoots. This is also the perfect time to edge garden beds, giving them a clean, defined look for the season.</p>

<h2>Soil Preparation</h2>
<p>Healthy plants start with healthy soil. Turn your compost pile and incorporate the finished compost into your garden beds. Conduct a soil test to determine pH and nutrient levels, then amend accordingly. Adding organic matter now will ensure your plants have the nutrients they need all season long.</p>

<h2>Early Spring Planting</h2>
<p>While it may still be too cold for tender annuals, many plants thrive in the cool spring temperatures:</p>
<ul>
  <li>Cold-tolerant vegetables like peas, spinach, and radishes</li>
  <li>Spring-flowering bulbs that weren't planted in fall</li>
  <li>Early-blooming perennials to add immediate color</li>
  <li>Trees and shrubs, which benefit from getting established before summer heat</li>
</ul>

<h2>Lawn Care</h2>
<p>Spring is a critical time for lawn maintenance. Rake thoroughly to remove thatch and stimulate growth. Apply pre-emergent herbicides before weed seeds germinate, and overseed bare patches. Hold off on heavy fertilization until later in the spring when grass is actively growing.</p>

<h2>Garden Decor Refresh</h2>
<p>Enhance your landscape with thoughtfully placed decorative elements:</p>
<ul>
  <li>Clean and repair garden structures, trellises, and hardscaping</li>
  <li>Inspect and update outdoor lighting for evening enjoyment</li>
  <li>Consider adding a water feature for visual interest and wildlife benefits</li>
  <li>Incorporate spring-themed garden stakes, ornaments, or sculptures</li>
</ul>

<p>By completing these essential tasks, you'll set your garden up for success throughout the growing season. The efforts you make now will be rewarded with lush growth, beautiful blooms, and a landscape that brings joy from spring through fall.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Garden Maintenance",
        "season": "Spring",
        "published_at": datetime(2025, 3, 15)
    },
    {
        "title": "Spring Color Guide: Best Flowers for Early Season Gardens",
        "slug": "spring-color-guide",
        "summary": "Discover the best flower varieties to plant for stunning spring colors and arrangements.",
        "content": """<p>After a long winter, the garden awakens with the promise of color. This guide will help you select the perfect flowers to create a vibrant spring display that captivates from the first warm day.</p>

<h2>Early Bloomers (March-April)</h2>
<p>These hardy flowers bring color while there's still a chill in the air:</p>
<ul>
  <li><strong>Crocus</strong> - Often the first to appear, sometimes even through snow</li>
  <li><strong>Snowdrops</strong> - Delicate white bells that naturalize beautifully</li>
  <li><strong>Hellebores</strong> - Long-lasting blooms in subtle shades of pink, green, and white</li>
  <li><strong>Daffodils</strong> - Classic yellow trumpets that signal spring has arrived</li>
  <li><strong>Primrose</strong> - Low-growing clusters in bright, cheerful colors</li>
</ul>

<h2>Mid-Spring Stars (April-May)</h2>
<p>The heart of spring brings an explosion of color options:</p>
<ul>
  <li><strong>Tulips</strong> - Available in virtually every color and numerous forms</li>
  <li><strong>Hyacinths</strong> - Fragrant spikes in jewel tones</li>
  <li><strong>Muscari (Grape Hyacinth)</strong> - Blue clusters that create stunning drifts</li>
  <li><strong>Fritillaria</strong> - Unique, bell-shaped flowers in unusual patterns</li>
  <li><strong>Bleeding Heart</strong> - Arching stems with distinctive heart-shaped blooms</li>
</ul>

<h2>Late Spring Transitions (May-June)</h2>
<p>These beauties bridge the gap between spring and summer gardens:</p>
<ul>
  <li><strong>Allium</strong> - Architectural spheres in purple, white, and pink</li>
  <li><strong>Columbine</strong> - Delicate, dancing flowers in an array of colors</li>
  <li><strong>Iris</strong> - Bold blooms with intricate details and patterns</li>
  <li><strong>Peony</strong> - Lush, romantic flowers with incredible fragrance</li>
  <li><strong>Late Tulips</strong> - Extend the tulip season with lily-flowered and parrot varieties</li>
</ul>

<h2>Design Strategies for Maximum Impact</h2>
<p>Create a dynamic spring garden with these design approaches:</p>
<ul>
  <li><strong>Layered Bulb Planting</strong> - Plant bulbs at different depths for successive blooms</li>
  <li><strong>Color Themes</strong> - Consider monochromatic schemes or complementary color pairs</li>
  <li><strong>Naturalizing</strong> - Allow bulbs to spread naturally in lawns or woodland areas</li>
  <li><strong>Container Combinations</strong> - Layer spring bulbs with cool-season annuals like pansies</li>
  <li><strong>Cutting Garden</strong> - Dedicate a space for flowers meant to be brought indoors</li>
</ul>

<p>By selecting a variety of spring bloomers with staggered flowering times, you'll ensure weeks of changing color and beauty. The joy of watching your spring garden unfold is one of the season's greatest pleasures, rewarding your winter patience with a spectacular display.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1460627390041-532a28402358?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Flowers & Plants",
        "season": "Spring",
        "published_at": datetime(2025, 4, 5)
    },
    # Summer
    {
        "title": "Summer Water Conservation: Smart Irrigation for Hot Months",
        "slug": "summer-water-conservation",
        "summary": "Learn effective water conservation techniques to keep your garden thriving during hot summer months.",
        "content": """<p>As temperatures rise and rainfall becomes less predictable, efficient water use becomes crucial for maintaining a beautiful garden while conserving this precious resource. This guide explores smart irrigation techniques specifically designed for the challenging summer months.</p>

<h2>Understanding Your Garden's Water Needs</h2>
<p>Not all plants require the same amount of water. Group plants with similar water requirements together (a technique called hydrozoning) to prevent overwatering some while underwatering others. Consider these general categories:</p>
<ul>
  <li><strong>High water use</strong> - Vegetables, newly planted specimens, container gardens</li>
  <li><strong>Moderate water use</strong> - Most perennial flowers, shrubs, and small trees once established</li>
  <li><strong>Low water use</strong> - Native plants, succulents, and drought-tolerant species</li>
</ul>

<h2>Irrigation Systems for Maximum Efficiency</h2>
<p>Choose the right watering method to minimize waste:</p>
<ul>
  <li><strong>Drip Irrigation</strong> - Delivers water directly to the root zone, reducing evaporation by up to 60% compared to sprinklers</li>
  <li><strong>Soaker Hoses</strong> - Excellent for rows of vegetables or perennial beds</li>
  <li><strong>Smart Controllers</strong> - Adjust watering schedules based on weather data and soil moisture</li>
  <li><strong>Rainwater Harvesting</strong> - Collect rainfall in barrels or cisterns for future use</li>
</ul>

<h2>Optimal Watering Techniques</h2>
<p>How and when you water makes a significant difference:</p>
<ul>
  <li><strong>Water deeply and infrequently</strong> - This encourages deeper root growth and creates more drought-resistant plants</li>
  <li><strong>Morning watering</strong> - Irrigate between 4am and 9am when evaporation rates are low and plants can dry before evening</li>
  <li><strong>Avoid overhead sprinklers</strong> - Especially during midday heat when up to 30% of water can be lost to evaporation</li>
  <li><strong>Use the screwdriver test</strong> - If a screwdriver easily penetrates 6-8 inches into the soil, you likely don't need to water</li>
</ul>

<h2>Garden Design for Water Conservation</h2>
<p>Long-term solutions for a more water-efficient garden:</p>
<ul>
  <li><strong>Apply mulch</strong> - A 2-3 inch layer reduces evaporation and moderates soil temperature</li>
  <li><strong>Improve soil structure</strong> - Add organic matter to increase water retention capacity</li>
  <li><strong>Create swales or rain gardens</strong> - Capture runoff and allow it to soak into the ground</li>
  <li><strong>Consider permeable hardscaping</strong> - Allow water to percolate rather than run off</li>
  <li><strong>Reduce lawn areas</strong> - Replace with drought-tolerant groundcovers or garden beds</li>
</ul>

<p>By implementing these water-wise practices, you can maintain a thriving garden even during the hottest months while being a responsible steward of environmental resources. The initial investment in efficient irrigation will pay dividends in both lower water bills and healthier plants.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1603574670812-d24560880210?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Sustainable Gardening",
        "season": "Summer",
        "published_at": datetime(2025, 6, 20)
    },
    {
        "title": "Ultimate Guide to Summer Container Gardens",
        "slug": "summer-container-gardens",
        "summary": "Create stunning summer container displays with these plant combinations and maintenance tips.",
        "content": """<p>Container gardens offer endless creative possibilities for summer color, even in small spaces or challenging environments. This comprehensive guide will help you design, plant, and maintain spectacular summer containers that will be the envy of your neighborhood.</p>

<h2>Selecting the Perfect Containers</h2>
<p>The right container sets the stage for your plant composition:</p>
<ul>
  <li><strong>Material considerations</strong> - Terracotta (porous, dries quickly), ceramic (retains moisture, heavy), metal (conducts heat), plastic (lightweight, retains moisture)</li>
  <li><strong>Size matters</strong> - Larger containers require less frequent watering and provide more room for roots</li>
  <li><strong>Drainage is essential</strong> - Ensure adequate drainage holes to prevent root rot</li>
  <li><strong>Style compatibility</strong> - Match containers to your home's architecture and garden style</li>
</ul>

<h2>Soil Secrets for Container Success</h2>
<p>Skip garden soil and opt for quality potting mix:</p>
<ul>
  <li><strong>Commercial potting mix</strong> - Provides proper aeration, drainage, and water retention</li>
  <li><strong>Custom blend</strong> - Mix equal parts potting soil, compost, and perlite or vermiculite</li>
  <li><strong>Water-retaining polymers</strong> - Consider adding these in hot climates to reduce watering frequency</li>
  <li><strong>Slow-release fertilizer</strong> - Incorporate at planting time for season-long nutrition</li>
</ul>

<h2>Plant Selection for Summer Heat</h2>
<p>Choose heat-tolerant plants that will thrive through summer's challenges:</p>

<h3>Sun-Loving Stars</h3>
<ul>
  <li><strong>Lantana</strong> - Butterfly magnet with multicolored blooms</li>
  <li><strong>Angelonia</strong> - "Summer Snapdragon" with vertical flower spikes</li>
  <li><strong>Calibrachoa</strong> - Prolific "Million Bells" in countless colors</li>
  <li><strong>Portulaca</strong> - Heat and drought resistant with succulent leaves</li>
  <li><strong>Ornamental Peppers</strong> - Colorful fruits that thrive in heat</li>
</ul>

<h3>Shade Container Champions</h3>
<ul>
  <li><strong>Begonias</strong> - Both foliage and flowering varieties perform well</li>
  <li><strong>Caladium</strong> - Dramatic foliage in shades of red, pink, and white</li>
  <li><strong>Coleus</strong> - Endless foliage patterns and colors</li>
  <li><strong>Fuchsia</strong> - Exotic-looking blooms for cooler shade areas</li>
  <li><strong>Impatiens</strong> - Reliable flowering in shady spots (New Guinea varieties are more sun-tolerant)</li>
</ul>

<h2>Design Principles for Eye-Catching Arrangements</h2>
<p>Follow the "thriller, filler, spiller" approach for professional-looking containers:</p>
<ul>
  <li><strong>Thriller</strong> - Tall, dramatic focal point planted in the center or back</li>
  <li><strong>Filler</strong> - Mounding plants that fill the middle space</li>
  <li><strong>Spiller</strong> - Trailing plants that cascade over the container edge</li>
</ul>

<h2>Summer Maintenance Essentials</h2>
<p>Keep your containers looking their best all season:</p>
<ul>
  <li><strong>Consistent watering</strong> - Check daily in peak summer; water when the top inch of soil is dry</li>
  <li><strong>Regular feeding</strong> - Apply liquid fertilizer every 1-2 weeks</li>
  <li><strong>Deadheading</strong> - Remove spent blooms to encourage more flowers</li>
  <li><strong>Pruning</strong> - Trim back leggy growth to maintain shape</li>
  <li><strong>Pest monitoring</strong> - Inspect regularly for insects and treat promptly</li>
</ul>

<p>With thoughtful planning and consistent care, your summer containers will provide months of vibrant color and texture. Don't be afraid to experiment with unexpected plant combinations - containers are the perfect place to express your creativity and try new garden ideas.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1611828856704-2ca5d9146321?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Flowers & Plants",
        "season": "Summer",
        "published_at": datetime(2025, 7, 10)
    },
    # Fall
    {
        "title": "Fall Garden Cleanup: Preparing for Winter While Supporting Wildlife",
        "slug": "fall-garden-cleanup",
        "summary": "Learn how to properly prepare your garden for winter while creating habitats for beneficial wildlife.",
        "content": """<p>Fall garden cleanup is often approached with a "cut it all down" mentality, but a more balanced approach benefits both your garden and local wildlife. This guide will help you prepare your garden for winter while supporting beneficial insects and animals that contribute to a healthy ecosystem.</p>

<h2>The Wildlife-Friendly Cleanup Approach</h2>
<p>Consider these principles when deciding what to cut back and what to leave standing:</p>
<ul>
  <li><strong>Selective cutting</strong> - Many perennials provide seeds for birds and nesting materials for beneficial insects</li>
  <li><strong>Habitat creation</strong> - Hollow stems and seed heads offer winter shelter for native bees and other beneficial insects</li>
  <li><strong>Disease management</strong> - Remove and dispose of diseased plant material; don't compost it</li>
  <li><strong>Aesthetic considerations</strong> - Many plants like ornamental grasses and seedheads of echinacea and rudbeckia provide winter interest</li>
</ul>

<h2>Plants to Cut Back in Fall</h2>
<p>Some plants benefit from fall pruning for health and appearance:</p>
<ul>
  <li><strong>Disease-prone perennials</strong> - Phlox, bee balm, and other plants susceptible to powdery mildew</li>
  <li><strong>Plants that become mushy</strong> - Hostas and other plants that collapse into unpleasant mush after frost</li>
  <li><strong>Self-seeders you want to control</strong> - Plants like black-eyed Susans that may spread too enthusiastically</li>
  <li><strong>Vegetable plants</strong> - Remove annual vegetables and their debris to reduce overwintering pests</li>
</ul>

<h2>Plants to Leave Standing for Wildlife</h2>
<p>These plants offer valuable resources for wildlife through winter:</p>
<ul>
  <li><strong>Coneflowers (Echinacea)</strong> - Seed heads provide food for goldfinches and other birds</li>
  <li><strong>Ornamental grasses</strong> - Offer shelter, nesting material, and winter interest</li>
  <li><strong>Joe-Pye weed</strong> - Hollow stems provide homes for native bees</li>
  <li><strong>Black-eyed Susans</strong> - Seeds feed birds throughout winter</li>
  <li><strong>Asters</strong> - Late-season nectar source and later, seeds for birds</li>
</ul>

<h2>Essential Fall Gardening Tasks</h2>
<p>Beyond plant cutbacks, focus on these important preparations:</p>
<ul>
  <li><strong>Soil care</strong> - Add compost to beds and plant cover crops in vegetable gardens</li>
  <li><strong>Mulching</strong> - Apply after ground freezes to prevent frost heaving</li>
  <li><strong>Leaf management</strong> - Shred leaves to use as mulch or add to compost; leave some in garden beds</li>
  <li><strong>Tool maintenance</strong> - Clean, sharpen, and oil tools before storing for winter</li>
  <li><strong>Water features</strong> - Clean and prepare fountains and ponds for winter</li>
</ul>

<h2>Fall Planting Opportunities</h2>
<p>Autumn is an excellent time for these additions to your garden:</p>
<ul>
  <li><strong>Spring-blooming bulbs</strong> - Plant tulips, daffodils, and other spring bulbs</li>
  <li><strong>Trees and shrubs</strong> - Fall planting allows roots to establish before summer heat</li>
  <li><strong>Cool-season vegetables</strong> - Grow lettuce, spinach, and other greens for fall harvest</li>
  <li><strong>Native plants</strong> - Establish habitat plants when rainfall is typically more abundant</li>
</ul>

<p>By taking this balanced approach to fall cleanup, you'll not only prepare your garden for a successful spring but also support the creatures that pollinate your flowers and help control garden pests. The dried seedheads and stems you leave standing will add winter interest to your garden landscape while providing essential resources for wildlife.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1508177524739-2d2a49f8c005?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Garden Maintenance",
        "season": "Fall",
        "published_at": datetime(2025, 9, 18)
    },
    {
        "title": "Fall Planting for Spring Splendor: Bulbs, Trees, and Perennials",
        "slug": "fall-planting-guide",
        "summary": "Discover what to plant in fall for a beautiful spring garden, including bulbs, trees, and perennial varieties.",
        "content": """<p>Fall is nature's preferred planting season, with cooler temperatures, more reliable rainfall, and less stress on new plants. This comprehensive guide will help you take advantage of autumn's ideal conditions to ensure a spectacular spring display and long-term garden success.</p>

<h2>Spring-Flowering Bulbs: Nature's Buried Treasure</h2>
<p>Fall is the only time to plant these spring-flowering favorites:</p>

<h3>Early Spring Bloomers (Plant in September-October)</h3>
<ul>
  <li><strong>Snowdrops</strong> - Often the first to emerge, sometimes even through snow</li>
  <li><strong>Crocus</strong> - Available in purples, yellows, whites, and striped varieties</li>
  <li><strong>Reticulated Iris</strong> - Diminutive but impactful early blooms</li>
  <li><strong>Winter Aconite</strong> - Cheerful yellow flowers that naturalize well</li>
</ul>

<h3>Mid-Spring Stars (Plant in October-November)</h3>
<ul>
  <li><strong>Daffodils</strong> - Reliable, pest-resistant, and available in many forms beyond classic yellow</li>
  <li><strong>Hyacinths</strong> - Intensely fragrant flowers in jewel tones</li>
  <li><strong>Tulips</strong> - Endless varieties from early species types to late double forms</li>
  <li><strong>Muscari (Grape Hyacinth)</strong> - Blue accents that return reliably for years</li>
</ul>

<h3>Late Spring Beauties (Plant in October-November)</h3>
<ul>
  <li><strong>Allium</strong> - Architectural spheres that bridge spring and summer</li>
  <li><strong>Camassia</strong> - Native star-shaped flowers for moist areas</li>
  <li><strong>Fritillaria</strong> - Unique checkerboard patterns or dramatic crown imperials</li>
  <li><strong>Ornamental Onions</strong> - Varied forms that thrive in poor soil</li>
</ul>

<h2>Fall Planting Tips for Bulbs</h2>
<p>Ensure bulb success with these essential techniques:</p>
<ul>
  <li><strong>Proper depth</strong> - Generally plant at a depth 3x the bulb's height</li>
  <li><strong>Good drainage</strong> - Add coarse sand to heavy soils to prevent rot</li>
  <li><strong>Grouping</strong> - Plant in clusters rather than single rows for natural appearance</li>
  <li><strong>Layering</strong> - Create a "bulb lasagna" in containers with different bloom times</li>
  <li><strong>Protection</strong> - Add hardware cloth below plantings if rodents are an issue</li>
</ul>

<h2>Trees and Shrubs: The Backbone of Your Landscape</h2>
<p>Fall is ideal for establishing woody plants:</p>
<ul>
  <li><strong>Deciduous trees and shrubs</strong> - Plant after leaf drop but before ground freezes</li>
  <li><strong>Fall color stars</strong> - Maple, oak, sweetgum, viburnum, and dogwood</li>
  <li><strong>Spring bloomers</strong> - Magnolia, redbud, serviceberry, and flowering fruit trees</li>
  <li><strong>Evergreens</strong> - Plant early fall to allow time for root establishment</li>
</ul>

<h2>Perennials That Benefit From Fall Planting</h2>
<p>Many perennials establish better when planted in fall:</p>
<ul>
  <li><strong>Peonies</strong> - Fall is the only recommended planting time</li>
  <li><strong>Iris</strong> - Divide and replant in early fall for best bloom</li>
  <li><strong>Spring bloomers</strong> - Bleeding heart, columbine, and creeping phlox</li>
  <li><strong>Native wildflowers</strong> - Many benefit from winter cold stratification</li>
  <li><strong>Ornamental grasses</strong> - Establish root systems before summer drought stress</li>
</ul>

<h2>Fall Planting Essentials</h2>
<p>Follow these best practices for successful establishment:</p>
<ul>
  <li><strong>Proper timing</strong> - Plant 4-6 weeks before ground freezes to allow for root growth</li>
  <li><strong>Thorough watering</strong> - Keep newly planted specimens well-hydrated until ground freezes</li>
  <li><strong>Mulching</strong> - Apply after ground cools to prevent frost heaving</li>
  <li><strong>No fertilizer</strong> - Avoid stimulating new growth that won't have time to harden off</li>
  <li><strong>Record keeping</strong> - Mark planting locations before winter arrives</li>
</ul>

<p>The effort you invest in fall planting will be richly rewarded when spring arrives. While your neighbors are just beginning to shop for their gardens, yours will already be bursting into bloom, giving you a head start on the growing season and years of enjoyment from well-established plants.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1597913323624-8a9904b91d00?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80", 
        "category": "Flowers & Plants",
        "season": "Fall",
        "published_at": datetime(2025, 10, 12)
    },
    # Winter
    {
        "title": "Winter Garden Planning: Designing Your Dream Landscape",
        "slug": "winter-garden-planning",
        "summary": "Use the winter months to plan next year's garden with these design tips and organizational strategies.",
        "content": """<p>Winter offers the perfect opportunity to evaluate your garden's performance and plan thoughtful improvements. With the landscape stripped to its essential structure, you can clearly see strengths and weaknesses. This guide will help you use the quiet season productively to ensure next year's garden exceeds your expectations.</p>

<h2>Reflection and Assessment</h2>
<p>Begin your planning process by evaluating what worked and what didn't:</p>
<ul>
  <li><strong>Photo review</strong> - Examine pictures from different seasons to identify gaps and successes</li>
  <li><strong>Winter interest</strong> - Note areas lacking visual appeal during dormant months</li>
  <li><strong>Maintenance hotspots</strong> - Identify areas that required excessive attention</li>
  <li><strong>Wildlife observations</strong> - Consider which garden areas supported birds, pollinators, and beneficial insects</li>
  <li><strong>Practical concerns</strong> - Assess pathways, drainage issues, and other functional aspects</li>
</ul>

<h2>Garden Mapping and Documentation</h2>
<p>Create a visual reference for your garden planning:</p>
<ul>
  <li><strong>Scale drawing</strong> - Sketch your existing landscape with measurements</li>
  <li><strong>Sun/shade mapping</strong> - Document light patterns through seasons</li>
  <li><strong>Plant inventory</strong> - Catalog existing plants with notes on performance</li>
  <li><strong>Soil testing</strong> - Winter is an ideal time to test soil and plan amendments</li>
  <li><strong>Hardscape assessment</strong> - Evaluate the condition of paths, walls, and other structures</li>
</ul>

<h2>Design Principles and Inspirations</h2>
<p>Consider these fundamental concepts for a cohesive garden:</p>
<ul>
  <li><strong>Focal points</strong> - Plan elements that draw the eye and create visual interest</li>
  <li><strong>Movement and flow</strong> - Ensure logical circulation through your space</li>
  <li><strong>Scale and proportion</strong> - Balance plant heights, hardscape elements, and open space</li>
  <li><strong>Unity and repetition</strong> - Create cohesion with recurring elements</li>
  <li><strong>Seasonal interest</strong> - Plan for attractive features in every season</li>
</ul>

<h2>Expanding Your Plant Palette</h2>
<p>Winter is the perfect time to research new plants:</p>
<ul>
  <li><strong>Garden books and magazines</strong> - Research during the quiet season</li>
  <li><strong>Seed catalogs</strong> - Early ordering ensures availability of popular varieties</li>
  <li><strong>Online plant databases</strong> - Research plants suited to your specific conditions</li>
  <li><strong>Native plant options</strong> - Identify indigenous species that thrive with minimal care</li>
  <li><strong>Specialty plants</strong> - Explore unique varieties that reflect your personal interests</li>
</ul>

<h2>Practical Planning Tools</h2>
<p>Organize your ideas with these helpful approaches:</p>
<ul>
  <li><strong>Garden journal</strong> - Document observations, plans, and plant information</li>
  <li><strong>Digital design tools</strong> - Try garden planning software or apps</li>
  <li><strong>Vision board</strong> - Collect images representing your garden goals</li>
  <li><strong>Project timeline</strong> - Create a realistic schedule for implementation</li>
  <li><strong>Budget planning</strong> - Allocate resources for priority projects</li>
</ul>

<h2>Exploring New Garden Trends</h2>
<p>Consider incorporating these contemporary approaches:</p>
<ul>
  <li><strong>Climate-adaptive gardening</strong> - Plan for weather extremes</li>
  <li><strong>Biodiversity enhancement</strong> - Create habitats supporting multiple species</li>
  <li><strong>Foodscaping</strong> - Integrate edibles into ornamental plantings</li>
  <li><strong>Sustainable water management</strong> - Plan rain gardens or bioswales</li>
  <li><strong>Vertical gardening</strong> - Maximize space by growing upward</li>
</ul>

<p>Winter garden planning allows you to approach the growing season with renewed purpose and vision. The quiet contemplation of these colder months often leads to the most thoughtful garden designs. By investing time now in careful planning, you'll create a landscape that not only delights the senses but also functions beautifully throughout the year.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1610406465776-5d3f1f1b1516?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Garden Design",
        "season": "Winter",
        "published_at": datetime(2025, 1, 15)
    },
    {
        "title": "Winter Garden Decor: Creating Beauty in the Dormant Season",
        "slug": "winter-garden-decor",
        "summary": "Transform your winter garden into a visual masterpiece with these decoration and design ideas.",
        "content": """<p>Winter gardens often go underappreciated, but with thoughtful design and strategic decorative elements, your landscape can shine even in the coldest months. This guide will help you create a winter garden that offers beauty, texture, and interest when other gardens lie dormant.</p>

<h2>Structural Elements: The Winter Garden Framework</h2>
<p>When foliage disappears, these elements become the stars:</p>
<ul>
  <li><strong>Architectural plants</strong> - Evergreens, topiary forms, and plants with distinctive branching patterns</li>
  <li><strong>Hardscaping</strong> - Walls, paths, and stairs gain prominence in winter</li>
  <li><strong>Garden structures</strong> - Arbors, trellises, and pergolas create visual interest and define spaces</li>
  <li><strong>Containers</strong> - Decorative pots and urns serve as focal points, especially when grouped</li>
  <li><strong>Stone features</strong> - Boulders, rock gardens, and stone walls add texture and permanence</li>
</ul>

<h2>Plants with Winter Appeal</h2>
<p>Incorporate these botanical standouts for winter interest:</p>

<h3>Bark and Stems</h3>
<ul>
  <li><strong>Red-twig dogwood</strong> - Brilliant scarlet stems intensify in cold weather</li>
  <li><strong>Paper birch</strong> - Peeling white bark creates striking contrast</li>
  <li><strong>Japanese maple</strong> - Elegant branching structure revealed when leaves drop</li>
  <li><strong>Coral bark maple</strong> - Salmon-colored branches glow in winter light</li>
  <li><strong>River birch</strong> - Exfoliating cinnamon-colored bark adds warmth</li>
</ul>

<h3>Evergreen Diversity</h3>
<ul>
  <li><strong>Blue spruce</strong> - Silver-blue needles brighten the winter landscape</li>
  <li><strong>Holly</strong> - Glossy leaves and bright berries offer classic winter beauty</li>
  <li><strong>Boxwood</strong> - Formal structure for garden bones</li>
  <li><strong>False cypress</strong> - Varied textures and colors from gold to blue</li>
  <li><strong>Broadleaf evergreens</strong> - Rhododendron, mountain laurel, and pieris provide leafy texture</li>
</ul>

<h3>Winter Bloomers</h3>
<ul>
  <li><strong>Witch hazel</strong> - Spidery blooms in yellow or copper appear on bare branches</li>
  <li><strong>Hellebores</strong> - "Christmas roses" bloom in late winter</li>
  <li><strong>Winter jasmine</strong> - Bright yellow flowers on arching stems</li>
  <li><strong>Camellia</strong> - Elegant flowers in winter to early spring</li>
  <li><strong>Winter heath</strong> - Low-growing carpets of tiny blooms</li>
</ul>

<h2>Decorative Elements for Winter Enhancement</h2>
<p>Add these decorative touches to elevate your winter garden:</p>
<ul>
  <li><strong>Outdoor lighting</strong> - Illuminate key features with uplighting, path lights, or string lights</li>
  <li><strong>Garden art</strong> - Sculptures, metal work, and decorative stakes become more visible</li>
  <li><strong>Bird features</strong> - Feeders, baths, and houses attract wildlife and movement</li>
  <li><strong>Decorative stakes and obelisks</strong> - Add vertical elements to complement dormant perennial beds</li>
  <li><strong>Winter containers</strong> - Arrange evergreen boughs, colorful twigs, and dried elements</li>
</ul>

<h2>Creating Winter Garden Rooms</h2>
<p>Designate spaces with specific winter appeal:</p>
<ul>
  <li><strong>Winter viewpoint</strong> - Design for visibility from indoor living spaces</li>
  <li><strong>Sheltered seating area</strong> - Create a protected spot to enjoy mild winter days</li>
  <li><strong>Sensory garden</strong> - Include winter-fragrant plants near paths</li>
  <li><strong>Winter vegetable garden</strong> - Cold frames and hoop houses add geometric structure</li>
  <li><strong>Fire feature area</strong> - Incorporate a fire pit or outdoor fireplace for warmth and gathering</li>
</ul>

<h2>Seasonal Maintenance for Winter Beauty</h2>
<p>Keep your winter garden looking its best:</p>
<ul>
  <li><strong>Strategic pruning</strong> - Prune selectively to highlight interesting branching patterns</li>
  <li><strong>Protective wrapping</strong> - Use burlap screens as decorative elements while protecting plants</li>
  <li><strong>Selective cleanup</strong> - Leave ornamental grasses and seed heads for texture and wildlife</li>
  <li><strong>Snow management</strong> - Plan for snow removal that enhances rather than damages the garden</li>
  <li><strong>Winter mulching</strong> - Apply decorative mulch in fall that will look attractive all winter</li>
</ul>

<p>By embracing winter's unique aesthetic opportunities, you'll develop a deeper appreciation for your garden during all seasons. A thoughtfully designed winter landscape offers meditative beauty during the quietest time of year, revealing the elegant structure that supports your garden's more exuberant seasons.</p>""",
        "featured_image": "https://images.unsplash.com/photo-1483664852095-d6cc6870702d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1200&q=80",
        "category": "Garden Decor",
        "season": "Winter",
        "published_at": datetime(2025, 12, 10)
    }
]

def main():
    try:
        # Start by checking if we already have blog posts
        existing_posts = BlogPost.query.all()
        if existing_posts:
            logging.info("Blog posts already exist. Skipping seed operation.")
            return
            
        # Add sample posts to the database
        for post_data in sample_posts:
            post = BlogPost(**post_data)
            db.session.add(post)
            
        # Commit the session to save all posts
        db.session.commit()
        logging.info(f"Successfully added {len(sample_posts)} blog posts to the database.")
    
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error seeding blog posts: {str(e)}")
        raise
        
if __name__ == "__main__":
    with app.app_context():
        main()