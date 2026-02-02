# الـ TOC بيظهر Chapter 1 بس بدون Sections

## المشكلة
الـ Table of Contents بيظهر:
```
1 INTRODUCTION ........................... 10
```

لكن المفروض يظهر:
```
1 INTRODUCTION ........................... 10
  1.1 Problem Definition ............... 11
  1.2 Importance of This Problem ....... 12
  1.3 Problem Solution ................. 13
  1.4 Project Objectives ............... 14
  1.5 System Features .................. 18
  1.6 Related Work ..................... 15
```

## السبب
الـ `.toc` file (Table of Contents file) مش متحدث. LaTeX بيحتاج **compile مرتين** عشان:
1. **المرة الأولى:** يكتب الـ sections في الـ `.toc` file
2. **المرة التانية:** يقرا الـ `.toc` file ويحطه في الـ PDF

## الحل

### الخطوة 1: امسح الملفات القديمة
```bash
# على Linux/Mac
rm -f *.aux *.log *.out *.toc *.lof *.lot

# على Windows PowerShell
Remove-Item *.aux, *.log, *.out, *.toc, *.lof, *.lot -ErrorAction SilentlyContinue

# أو على Windows CMD
del *.aux *.log *.out *.toc *.lof *.lot
```

**مهم جداً:** لازم تمسح الـ `.toc` file القديم!

### الخطوة 2: اعمل Compile مرتين
```bash
# المرة الأولى
xelatex main.tex

# المرة التانية (مهمة جداً!)
xelatex main.tex
```

**ملحوظة:** لو بتستخدم IDE زي TeXstudio أو Overleaf، اعمل compile مرتين من الـ IDE.

### الخطوة 3: تحقق من النتيجة
افتح الـ PDF - المفروض الـ TOC يظهر كده:

```
Table of Contents

1 INTRODUCTION ........................... 10
  1.1 Problem Definition ............... 11
  1.2 Importance of This Problem ....... 12
  1.3 Problem Solution ................. 13
  1.4 Project Objectives ............... 14
  1.5 System Features .................. 18
  1.6 Related Work ..................... 15
```

## التحقق من الـ Sections

الـ sections في Chapter 1 موجودة وصحيحة:

### في `content/chapter1-new/problem-definition.tex`:
```latex
\section{1.1 Problem Definition}
\label{sec:problem-definition}
```

### في `content/chapter1-new/importance.tex`:
```latex
\section{1.2 Importance of This Problem}
\label{sec:importance}
```

### في `content/chapter1-new/solution.tex`:
```latex
\section{1.3 Problem Solution}
\label{sec:solution}
```

### في `content/chapter1-new/objectives.tex`:
```latex
\section{1.4 Project Objectives}
\label{sec:objectives}
```

### في `content/chapter1-new/features.tex`:
```latex
\section{1.5 System Features}
\label{sec:features}
```

### في `content/chapter1-new/related-work.tex`:
```latex
\section{1.6 Related Work}
\label{sec:related-work}
```

كل الـ sections بتستخدم `\section` العادي (مش `\section*`)، وده صح! ✅

## الإعدادات الحالية

في `config.tex`:
```latex
\setcounter{tocdepth}{1}      % Show chapters and sections
\setcounter{secnumdepth}{3}   % Number up to subsubsections
```

ده معناه:
- ✅ الـ TOC هيظهر: Chapters + Sections
- ❌ الـ TOC مش هيظهر: Subsections (1.1.1, 1.1.2, etc.)

## ليه LaTeX بيحتاج Compile مرتين؟

### المرة الأولى:
1. LaTeX بيقرا `main.tex`
2. بيلاقي `\tableofcontents`
3. بيدور على ملف `main.toc`
4. مش بيلاقيه (أو بيلاقيه قديم)
5. بيكتب TOC جديد في `main.toc`
6. بيحط placeholder في الـ PDF

### المرة التانية:
1. LaTeX بيقرا `main.tex` تاني
2. بيلاقي `\tableofcontents`
3. بيقرا `main.toc` (اللي اتعمل في المرة الأولى)
4. بيحط الـ TOC الصحيح في الـ PDF ✅

## لو المشكلة لسه موجودة

### 1. تأكد إن الـ .toc file موجود
```bash
ls -la main.toc
# أو على Windows
dir main.toc
```

لو الملف موجود، افتحه وشوف محتواه:
```bash
cat main.toc
# أو على Windows
type main.toc
```

المفروض تشوف حاجة زي:
```latex
\contentsline {chapter}{\numberline {1}INTRODUCTION}{10}{}
\contentsline {section}{\numberline {1.1}Problem Definition}{11}{}
\contentsline {section}{\numberline {1.2}Importance of This Problem}{12}{}
...
```

### 2. تأكد إن مفيش errors في الـ compile
شوف الـ `main.log` file ودور على:
```
! LaTeX Error
```

### 3. جرب compile 3 مرات
أحياناً LaTeX بيحتاج 3 مرات لو في cross-references كتير:
```bash
xelatex main.tex
xelatex main.tex
xelatex main.tex
```

### 4. استخدم latexmk (أوتوماتيكي)
```bash
latexmk -xelatex main.tex
```

الـ `latexmk` بيعمل compile أوتوماتيكي لحد ما كل حاجة تبقى صح.

## الخلاصة

✅ **الـ sections موجودة وصحيحة**
✅ **الإعدادات صحيحة (`tocdepth=1`)**
❌ **لازم compile مرتين عشان الـ TOC يتحدث**

### الخطوات:
1. امسح `*.toc` و `*.aux`
2. اعمل `xelatex main.tex`
3. اعمل `xelatex main.tex` تاني
4. افتح الـ PDF

المفروض دلوقتي الـ sections تظهر في الـ TOC! 🎉

---

**ملحوظة:** لو عملت الخطوات دي والمشكلة لسه موجودة، ابعتلي محتوى الـ `main.toc` file عشان أشوف إيه المشكلة.
