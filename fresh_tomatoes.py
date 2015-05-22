import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
     <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 100px;
            width: 1000px;
            height: 600px;
        }
        #trailer .modal-content{
	    width:100%;
	    height:100%;
	    float:right;
	    background-color: black;	
	}
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
	    height:100%;
            padding-bottom: 35%;
            position: relative;
	    background-color: black;
        }
        .scale-media iframe {
            border: none;
            height: 400px;
            position: absolute;
            width: 640px;
	    float:left;
            right: 0;
            bottom: 0;
            background-color: black;
        }
	.modal-poster-div{
	  width:350px;
	  height:100%;
	  float:left;
	  position:relative;	
	}
	.storylineText {
	  width:640px;
	  float:right;
	  height:150px;
	  position:relative;
	  color:white;	
	  padding:15px;
	}
    </style>
     <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
	  //it takes too much time to figure out why, but clicking in the black behind the video closes everything with this system
	  //as I don't know how the attached modal system works, this is a better solution than the alternative which is the video continues playing after closing the popup
          location.reload()
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
	    var posterSource = $(this).attr('img-source-id')
	    var storyline = $(this).attr('storyline')
	    //$(this).attr('img_source_id')
	    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
	    //$("#modal-dialog").empty().append($("<img src="posterSource"></img>"))
	    //$("#trailer-video-container").append($("<iframe></iframe>", {'id': 'trailer-video','type': 'text-html','src': sourceUrl,'frameborder': 0 }));
	    var movieDisplayHtml = "<div class='modal-poster-div'><img width='100%' src='"+posterSource+"'></img></div><div class='storylineText'>"+storyline+"</div><iframe src='"+sourceUrl+"'height='100px'></iframe>"
	    $("#trailer-video-container").html(movieDisplayHtml);
        });
        
        
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" img-source-id="{poster_image_url}" storyline="{storyline}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
	    storyline =movie.storyline,
            trailer_youtube_id=trailer_youtube_id
	    
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  with open('fresh_tomatoes.html','w') as output_file:
  #output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  	rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  	output_file.write(main_page_head + rendered_content)
  #output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
