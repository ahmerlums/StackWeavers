For part 1, run python par1.py directory
For part2,
 Run python part2.py, and using a browser to open link "localhost:8080/index.html"
 Valid Paths are  "localhost:8080/index.html","localhost:8080/home.html" and "localhost:8080/files/abc.pdf" and 200 OK is returned for them.
 For rest(invalid paths)  404 NOT FOUND is returned.
 Also, you can make a POST or HEAD request from Postman.
 For Post, you need to send something in the form input to have 403 Created returned. Empty form would result in 422 Unprocessable Entity.
