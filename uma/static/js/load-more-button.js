$( document ).ready(function () {
                $(".moreBox").slice(0, 3).show();
                if ($(".blogBox:hidden").length != 0) {
                        $("#loadMore").show();
                }
                $("#loadMore").on('click', function (e) {
                        e.preventDefault();
                        $(".moreBox:hidden").slice(0, 6).slideDown();
                        if ($(".moreBox:hidden").length == 0) {
                                $("#loadMore").fadeOut('slow');
                        }
                });
        });


// Media Gaallery Image Pop Up
  $( document ).ready(function enlargeImg() {
          var modal = document.getElementById("myModal");

          // Get the image and insert it inside the modal - use its "alt" text as a caption
          var img = document.getElementById("myImg");
          var modalImg = document.getElementById("img01");
          // var captionText = document.getElementById("caption");
          img.onclick = function(){
            modal.style.display = "block";
            modalImg.src = this.src;
            //captionText.innerHTML = this.alt;
          }

          // Get the <span> element that closes the modal
          var span = document.getElementsByClassName("close")[0];

          // When the user clicks on <span> (x), close the modal
          span.onclick = function() {
            modal.style.display = "none";
          }
        });
