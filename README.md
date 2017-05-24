# UpUp Essays

This plugin is used to present essays inside a MarkUpUpDownDown site.

The plugin works such that any content directory where the `essays` plugin is called will:

1. look one level below for essays (content directories)
2. render each essay
3. produce a list of essays sorted by creation date


## Installing

To install, just type `pip install upup_essays` and add `essays` to your project config.

```yaml
---
content_dir: "./content"
...
plugins:
    - essays
```

Then run the install command to copy copy over the relevant templates and static data:

```shell
$ markupupdowndown essays install
```

## Content Structure

The essays directory, eg. `/content/essays`, would have an `index.md` that looks like this:

```
---
title: Essays
plugin: essays
template: "essays/base.html"
---
```

The essays directory can be created like this:

```shell
$ markupupdowndown new essays
```

Each essay then exists in a content directory below, like `/content/essays/some-essay-i-wrote` or `/content/essays/another-essay`.

The URL for your essays, like `http://some.com/content/essays`, would produced a rendered list of links for each essay.

Essay directories are just standard content directories and can be created with MarkUpUpDownDown's `new content` command


## Real Example

You can check out the way jmsdnns.com uses this plugin here [here](https://github.com/jmsdnns/jmsdnns.com/tree/master/content/essays) and the rendered output is [here](http://jmsdnns.com/essays).
