# How to make a release for DxSter with git flow

author(s): Philip B. Chase(https://github.com/pbchase), Christopher P. Barnes (http://github.com/senrabc)

When some software is ready to be released, it needs to be released within source control first.  In short, it needs a version number, a tag, a Change log update and it needs to be merged into master.  You can do all of these things with Git Flow and this procedure.  

Begin with a local clone of the repository you are going to release.

<pre>
git clone repository_uri
</pre>

cd into the repository directory, and do "git remote -v" to verify that you are pulling from the correct repository.

Make sure you have the latest commits:
<pre>
git checkout master && git pull && git checkout develop && git pull && git fetch --tags && git tag
</pre>

Check the for the next release number by looking at the set tags. If this is the initial release of a repo, it will return a blank response. You won't see "0.0.0".

<pre>
git tag
</pre>

Start a release branch with the next major version number in the series.

*NOTE:* if you have not used git flow in this repository before, you will need to run "git flow init" in the directory. Accept all the default settings for setting up git flow unless your project documentation specifies otherwise. In the example below you would change the "0.4.0" to whatever number you are going to with your release.

<pre>
git flow release start 0.4.0
</pre>

Make a note of the changes you made in the CHANGELOG.  A good first start to describe what you did would be to enumerate the commits you added.  Any git log output that displays one commit per line would help.  This git alias in your .gitconfig file (located in your home directory at ~/.gitconfig) could help:

<pre>
[alias]
    chlog = log --color --no-merges --pretty=format:' * %s (%an)'
</pre>

Then you can do this:

<pre>
git chlog 0.3.1..HEAD
</pre>

For the above example, it shows the number prior to the tag you are releasing. This implies that the tag you are going to is 0.3.2.

But please, please, please _summarize_ the commits displayed into the overall change.  The Change Log is _not_ meant to be a repeat of the commit history.

DxSter uses the http://keepachangelog.com/ standard for its Change Logs.  Please refer to the http://keepachangelog.com/ website for complete details.  
These Change Logs look like this:

<pre>
## [4.0.12] - 2015-08-25
### Changed
* Make event table colors consistent

## [4.0.11] - 2015-08-25

### Changed
* Update pattern matching in Makefile (Philip Chase)
* Use static arrays to hardcode list of days in EventTablesController (Kevin Hanson)

### Added
* Add schema 4.0.11 to puphpet/files/exec-once/02_init_db.sh (Philip Chase)
* Add two columns to `lu_form_days` so we can track the time of changes (Philip Chase)
</pre>

For a some types of release, you have to update the version number in two places.
* CHANGELOG, in the summary line
* setup.py, change the following line to reflect the new version:
download_url = 'https://github.com/ctsit/dxster/releases/tag/0.15.1',

If your project has documents on ReadTheDocs, bump the version number in docs/conf.py. Change the following two lines:

<pre>
# The short X.Y version.
version = '0.14.2'
# The full version, including alpha/beta/rc tags.
release = '0.14.2'
</pre>

If there is another location where the new version number should be reflected, make that change as well. I.E.,  Python projects have the version number in their setup.py file.

Now commit the changes to the CHANGELOG and another other files you changed to do the release

<pre>
git add CHANGELOG setup.py
git commit -m "Update CHANGELOG and setup.py for release 0.4.0"
</pre>

Close out new release.  This will merge the new commits master.

For the next step make sure you write a tag message because if you don't then your git flow release finish will FAIL

<pre>
git flow release finish 0.4.0
</pre>

Git Flow will request request three commit messages.  The second one is the message on the Tag for this release.  At DxSter we pass the relevant portion of the CHANGELOG into the commit message editing out the #s to assure the Change Log lines will not be interpreted as comments.

Push the commits for both branches.  Also, make sure you push the tags.  Assuming you are still on the develop branch, the command would look like this:

<pre>
git push
git checkout master
git push
git push --tags
git checkout develop
</pre>

Or, if you like to chain commands together, do this:

<pre>
git push && git checkout master && git push && git push --tags && git checkout develop
</pre>

*NOTE:* Don't forget to make a new release on GitHub based on your tag through the GitHub web interface. Also, close any GitHub issues that were fixed by this release.
