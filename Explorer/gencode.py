def generate_html(urls: list, titles: list) -> str:
    if len(urls) != len(titles):
        raise ValueError("The length of urls and titles must be the same.")

    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Grid with Paging</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet">
    <style>
                body, html {
                margin: 0;
                padding: 0;
                height: 100%;
            }
            .color-controls {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                padding: 10px;
                background-color: #f0f0f0;
                z-index: 1000;
                display: flex;
                justify-content: space-around;
            }
            .grid-container {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(256px, 1fr));
                gap: 10px;
                padding: 20px;
                padding-top: 60px; /* space for color controls */
            }
            .grid-container img {
                max-width: 100%;
                height: auto;
                border: 1px solid #ccc;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            }
            .background {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1;
            }
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: 'Roboto', sans-serif;
        }
        .controls {
                padding: 10px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: rgba(240, 240, 240, 0.7); /* Blurry-transparent background */
            backdrop-filter: blur(10px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: space-around;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(256px, 1fr));
            gap: 10px;
            padding: 20px;
            padding-top: 80px; /* space for controls */
        }
        .grid-item {
            position: relative;
            text-align: center;
        }
        .grid-item img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ccc;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        .grid-item span {
            display: block;
            font-size: 8pt;
            color: #333;
            margin-bottom: 5px;
            display: none; /* Initially hidden */
        }


                <label><input type="checkbox" id="toggle-titles"> Show Titles</label>

    </style>
</head>
<body>
    <div class="controls">
        <span class="title">MAGICK Explorer</span>
            <input type="color" id="color1" value="#56eb34">
            <input type="color" id="color2" value="#5834eb">
        <input type="text" id="search" placeholder="Enter search term...">
        <span id="search-result-count"></span>
        <label><input type="checkbox" id="toggle-titles"> Show Titles</label>
        <button id="prev-page">Prev Page</button>
        <span id="page-info"></span>
        <button id="next-page">Next Page</button>
        <input type="number" id="goto-page" placeholder="Go to page...">
        <button id="set-page">Go</button>
        <label>Images per page: <input type="number" id="images-per-page" value="1000"></label>
    </div>
    <div class="background"></div>
    <div class="grid-container"></div>
    <script>
        var urls = """ + str(urls) + """;
        var titles = """ + str(titles) + """;
        var currentPage = 1;
        var imagesPerPage = 100;
        var filteredUrls = [];
        var filteredTitles = [];

        function renderImages() {
            var container = document.querySelector('.grid-container');
            container.innerHTML = '';
            var startIndex = (currentPage - 1) * imagesPerPage;
            var endIndex = startIndex + imagesPerPage;
            for (var i = startIndex; i < endIndex && i < filteredUrls.length; i++) {
                var imgDiv = '<div class="grid-item"><span>' + filteredTitles[i] + '</span><img src="' + filteredUrls[i] + '" alt="Image" class="image"></div>';
                container.innerHTML += imgDiv;
            }
            document.getElementById('page-info').innerText = 'Page ' + currentPage + '/' + Math.ceil(filteredUrls.length / imagesPerPage);
        }
        
            function updateBackground() {
                var color1 = document.getElementById('color1').value;
                var color2 = document.getElementById('color2').value;
                document.querySelector('.background').style.background = 'linear-gradient(to bottom, ' + color1 + ', ' + color2 + ')';
            }
            document.getElementById('color1').addEventListener('input', updateBackground);
            document.getElementById('color2').addEventListener('input', updateBackground);
            
        setTimeout(window.updateBackground, 3000); // 500 milliseconds = 0.5 seconds
        

        function searchImages() {
            var searchTerm = document.getElementById('search').value.toLowerCase();
            filteredUrls = [];
            filteredTitles = [];
            for (var i = 0; i < urls.length; i++) {
                if (titles[i].toLowerCase().includes(searchTerm)) {
                    filteredUrls.push(urls[i]);
                    filteredTitles.push(titles[i]);
                }
            }
            currentPage = 1;
            renderImages();
            document.getElementById('search-result-count').innerText = filteredUrls.length + ' results';
        }

        document.getElementById('search').addEventListener('input', searchImages);
        document.getElementById('next-page').addEventListener('click', function() {
            if (currentPage * imagesPerPage < filteredUrls.length) {
                currentPage++;
                renderImages();
            }
        });
        document.getElementById('prev-page').addEventListener('click', function() {
            if (currentPage > 1) {
                currentPage--;
                renderImages();
            }
        });
        document.getElementById('set-page').addEventListener('click', function() {
            var goToPage = parseInt(document.getElementById('goto-page').value);
            if (goToPage && goToPage > 0 && goToPage <= Math.ceil(filteredUrls.length / imagesPerPage)) {
                currentPage = goToPage;
                renderImages();
            }
        });
        document.getElementById('images-per-page').addEventListener('change', function() {
            imagesPerPage = parseInt(document.getElementById('images-per-page').value);
            currentPage = 1;
            renderImages();
        });

        // Initialize with all images
        searchImages();
    </script>
</body>
</html>
"""

    return html

def process(urls,titles):
    output=[]
    for url,title in zip(urls,titles):
        try:
            url=eval(url)
            output.append([url,title])
        except Exception:
            pass
    return list_transpose(output)
    
rows=random_batch_up_to(csv,100000)
urls=rows.URL
titles=rows.TEXT
urls,titles=process(urls,titles)
html=generate_html(urls,titles)
string_to_text_file('test.html',html)
