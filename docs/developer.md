# Workflow

This documentation describes how to work with the GitHub repository. Required tools are _VS Code_ and _Windows Subsystem for Linux_.

## 1. Fork in the GitHub

1. Visit https://github.com/bcgov/ppr
1. Click the _Fork_ button (top right)

## 2. Clone the Fork to your Workstation

In VS Code, go to _View > Command Palette_, enter _Git: Clone_. Enter the URL of your clone (`https://github.com/[username]/ppr`). Give a location for your local copy (such as `C:\Users\[username]\VSCode`).

In VS Code, go to _View > Command Palette_, enter _Git: Add Remote_. For the _Remote name_ enter `upstream` and for the _Remote URL_ enter `https://github.com/bcgov/ppr`.

The next step needs to be done on the command line. In VS Code go to _Terminal > New Terminal_ and run:

```sh
$ git remote set-url --push upstream no_push
$ git remote -v
origin  https://github.com/[username]/ppr (fetch)
origin  https://github.com/[username]/ppr (push)
upstream        https://github.com/bcgov/ppr (fetch)
upstream        no_push (push)
```

This will prevent accidentally pushing to the main repository.

## 3. Branch your Code

In the bottom-left corner of VS Code is the Source Control logo with the name of your current branch. Ensure that it is _master_. If not, click the branch name and then select _master_ from the list of branches.

After your first clone you will be up to date, but if you return to this step in the future you will want to ensure that your local master is up to date:

```sh
$ git fetch upstream
From https://github.com/bcgov/ppr
 * [new branch]      master     -> upstream/master
$ git rebase upstream/master
Current branch master is up to date.
```

Click the Source Control logo in the bottom-left corner of VS Code and select _Create new branch..._. Name your branch with the format `1-branch_description`, where `1` is the GitHub Issue number that you are working on.

Notice that in the bottom-left corner you have checked out the new branch.

## 4. Keep your Branch in Sync

While you are working on the changes in your branch, ensure that you stay up to date with the main repository. This will reduce merge problems.

```sh
$ git fetch upstream
$ git rebase upstream/master
Current branch 1-branch_description is up to date.
```

Please don't use _git pull_ instead of the above _fetch / rebase_. _git pull_ does a merge, which leaves merge commits. These make the commit history messy and violate the principle that commits ought to be individually understandable and useful (see below). You can also consider changing your `.git/config` file via `git config branch.autoSetupRebase always` to change the behaviour of `git pull` (TODO: details on this, couldn't get it to work).

## 5. Commit

In the VS Code left hand navigation, click the Source Control logo to bring up the view.

In VS Code you need to Stage your changes before commiting. To stage files that are added or edited, either right-click the file and select _Stage Changes_ or click the _+_ symbol to the right of the filename.

When ready to commit, enter a message in the text box at the top of the Source Control view. Your message should end with the Issue number you are working on, such as "_Description of my changes #1_". CTRL-Enter will commit the staged changes.

## 6. Push

When ready to review (or just to establish an offsite backup of your work), push your branch to your fork on GitHub. In VS Code open the Source Control view and click the ... menu and select _Push to..._ and select _origin_.

## 7. Create a Pull Request

TODO: Create a PR template and document it.

1. Visit your fork on GitHub and go to the list of branches that you have.
1. Click the _New pull request_ button next to your _1-branch_description_ branch.
1. Carefully review all of your changes to ensure that you have not committed anything by accident. Only changes related to the Issue you're working on should be included. If necessary create additional Issues for unrelated changes.
1. TODO: describe how to fill in the comment template.

#### Get Code Reviews

Once your Pull Request has been opened, assign it to one or more reviewers. Those reviewers will do a thorough code review, looking for correctness, bugs, opportunities for improvement, documentation and comments, and style.

Commit changes made in response to review comments to the same branch on your fork.

Very small PRs are easy to review. Very large PRs are very difficult to review.

#### Squash and Merge

Upon merge (by either you or your reviewer), all commits left on the review branch should represent meaningful milestones or units of work. Use commits to add clarity to the development and review process.

Before merging a PR, squash any _fix review feedback_, _typo_, _merged_, and _rebased_ sorts of commits.

It is not imperative that every commit in a PR compile and pass tests independently, but it is worth striving for.

In particular, if you happened to have used `git merge` and have merge commits, please squash those away: they do not meet the above test.

A nifty way to manage the commits in your PR is to do an [interactive rebase](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History), which will let you tell git what to do with every commit:

```sh
$ git fetch upstream
$ git rebase -i upstream/master
```

For mass automated fixups (e.g. automated doc formatting), use one or more commits for the changes to tooling, and a final commit to apply the fixup en masse. This makes reviews easier.

## 8. Branch Cleanup

You will now have some cleanup to do with the branches that you have created. In GitHub go to your repository and list your branches. Click the red garbage can icon next to your branch to delete it.

In VS Code you will also want to delete your branch. You cannot delete the branch you have checked out, so click the Source Control logo in the bottom-left corner of VS Code and choose _master_ to check it out. Then go to _View > Command Palette_, enter _Git: Delete Branch..._ and select the branch to be deleted.

## 9. Sync your Fork

To keep your fork on GitHub up to date, you will now want to sync it. Ensure that you are in the master branch, and do the following:

```sh
$ git fetch upstream
$ git rebase upstream/master
$ git push
```

## Attribution

This page heavily borrowed from the kubernetes.io project - thanks from our Registries team.

Hey there -- test
