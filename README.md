# Cal State Fullerton - ACM-W Website
## *static HTML branch*

## *to mirror Flask version*
1. clone the repo: `$ git clone https://github.com/ACM-W/ACMW-refresh.git`
2. `cd` into the new directory: `$ cd ACMW-refresh`
3. install flask and other requirements: `$ pip install -r requirements.txt`
  - if you want, you can do this inside of a virtualenv
4. tell flask where to find the app: `$ export FLASK_APP=app.py` or `$ set FLASK_APP=app.py`
5. *optionally*, turn on flask's debug mode: `$ export FLASK_DEBUG=1` or `$ set FLASK_DEBUG=1`
6. **run the development server**: `$ flask run`
7. Spider the site: `$ wget -mk http://localhost:5000`
8. `cd` into the new mirror directory: `$ cd localhost:5000`
9. Rename files to end in .html (e.g., `$ mv board board.html`)
10. Browse to `http://localhost:5000/events` and save a copy of the page as `events.html`
11. Manually edit files to use HTML links (e.g., change `href=board` to `href=board.html`)

### TODO
 - [ ] Learn to use a static site generator
   (e.g., <https://jekyllrb.com/> or <https://getnikola.com/>).

