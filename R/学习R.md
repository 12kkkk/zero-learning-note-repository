# 学习R

    # 学习过程的各种代码、函数保存在目录：A:/Rstudio/学习R 下，学习R.R    学习R.RData
    path = 'A:/Rstudio/学习R'

## 1、R入门

基本的R命令

    help()   # 获得帮助

    ## starting httpd help server ... done

    help.start() # R语言的入门帮助

    ## If nothing happens, you should open
    ## 'http://127.0.0.1:28639/doc/html/index.html' yourself

    help('')  # 输入函数，获得函数的帮助

    ## No documentation for '' in specified packages and libraries:
    ## you could try '??'

    example('')  # 输入函数，获得函数使用示例

    ## Warning in example(""): no help found for ''

    data()  # 查看内置数据集，输入数据集名称，未输入数据集名称则列出数据集信息

    getwd() # 获得当前工作路径

    ## [1] "A:/Rstudio/学习R"

    # setwd() # 设置工作路径
    dir() # 查看当前工作目录下的文件

    ##  [1] "file_name.xlsx"      "images"              "merged_output.xlsx" 
    ##  [4] "RNA_seq.Rmd"         "Rplot.tiff"          "R语言可视化.Rmd"    
    ##  [7] "死亡率_方差分析.Rmd" "学习R.html"          "学习R.RData"        
    ## [10] "学习R.Rmd"           "学习R_数据"

    ls()  # 列出当前工作环境的变量

    ## [1] "path"

    rm()  # 移除指定变量

    # history()  #查看历史命令

    save.image('.RData')  # 保存工作映像

    options()  # 

    ## $add.smooth
    ## [1] TRUE
    ## 
    ## $browserNLdisabled
    ## [1] FALSE
    ## 
    ## $callr.condition_handler_cli_message
    ## function (msg) 
    ## {
    ##     custom_handler <- getOption("cli.default_handler")
    ##     if (is.function(custom_handler)) {
    ##         custom_handler(msg)
    ##     }
    ##     else {
    ##         cli_server_default(msg)
    ##     }
    ## }
    ## <bytecode: 0x00000280caa07ae0>
    ## <environment: namespace:cli>
    ## 
    ## $catch.script.errors
    ## [1] FALSE
    ## 
    ## $CBoundsCheck
    ## [1] FALSE
    ## 
    ## $check.bounds
    ## [1] FALSE
    ## 
    ## $citation.bibtex.max
    ## [1] 1
    ## 
    ## $continue
    ## [1] "+ "
    ## 
    ## $contrasts
    ##         unordered           ordered 
    ## "contr.treatment"      "contr.poly" 
    ## 
    ## $defaultPackages
    ## [1] "datasets"  "utils"     "grDevices" "graphics"  "stats"     "methods"  
    ## 
    ## $demo.ask
    ## [1] "default"
    ## 
    ## $deparse.cutoff
    ## [1] 60
    ## 
    ## $device
    ## function (width = 7, height = 7, ...) 
    ## {
    ##     grDevices::pdf(NULL, width, height, ...)
    ## }
    ## <bytecode: 0x00000280cb24a7d0>
    ## <environment: namespace:knitr>
    ## 
    ## $device.ask.default
    ## [1] FALSE
    ## 
    ## $digits
    ## [1] 7
    ## 
    ## $echo
    ## [1] FALSE
    ## 
    ## $editor
    ## [1] "notepad"
    ## 
    ## $encoding
    ## [1] "native.enc"
    ## 
    ## $example.ask
    ## [1] "default"
    ## 
    ## $expressions
    ## [1] 5000
    ## 
    ## $help.search.types
    ## [1] "vignette" "demo"     "help"    
    ## 
    ## $help.try.all.packages
    ## [1] FALSE
    ## 
    ## $help_type
    ## [1] "html"
    ## 
    ## $htmltools.preserve.raw
    ## [1] TRUE
    ## 
    ## $HTTPUserAgent
    ## [1] "R (4.5.1 x86_64-w64-mingw32 x86_64 mingw32)"
    ## 
    ## $install.packages.compile.from.source
    ## [1] "interactive"
    ## 
    ## $internet.info
    ## [1] 2
    ## 
    ## $keep.parse.data
    ## [1] TRUE
    ## 
    ## $keep.parse.data.pkgs
    ## [1] FALSE
    ## 
    ## $keep.source
    ## [1] FALSE
    ## 
    ## $keep.source.pkgs
    ## [1] FALSE
    ## 
    ## $knitr.in.progress
    ## [1] TRUE
    ## 
    ## $locatorBell
    ## [1] TRUE
    ## 
    ## $mailer
    ## [1] "mailto"
    ## 
    ## $matprod
    ## [1] "default"
    ## 
    ## $max.contour.segments
    ## [1] 25000
    ## 
    ## $max.print
    ## [1] 99999
    ## 
    ## $menu.graphics
    ## [1] TRUE
    ## 
    ## $na.action
    ## [1] "na.omit"
    ## 
    ## $nwarnings
    ## [1] 50
    ## 
    ## $OutDec
    ## [1] "."
    ## 
    ## $pager
    ## [1] "internal"
    ## 
    ## $papersize
    ## [1] "a4"
    ## 
    ## $PCRE_limit_recursion
    ## [1] NA
    ## 
    ## $PCRE_study
    ## [1] FALSE
    ## 
    ## $PCRE_use_JIT
    ## [1] TRUE
    ## 
    ## $pdfviewer
    ## [1] "B:/R-4.5.1/bin/x64/open.exe"
    ## 
    ## $pkgType
    ## [1] "both"
    ## 
    ## $prompt
    ## [1] "> "
    ## 
    ## $repos
    ##     CRAN 
    ## "@CRAN@" 
    ## 
    ## $rlang_trace_top_env
    ## <environment: R_GlobalEnv>
    ## 
    ## $scipen
    ## [1] 0
    ## 
    ## $show.coef.Pvalues
    ## [1] TRUE
    ## 
    ## $show.error.messages
    ## [1] TRUE
    ## 
    ## $show.signif.stars
    ## [1] TRUE
    ## 
    ## $showErrorCalls
    ## [1] TRUE
    ## 
    ## $showNCalls
    ## [1] 50
    ## 
    ## $showWarnCalls
    ## [1] FALSE
    ## 
    ## $str
    ## $str$strict.width
    ## [1] "no"
    ## 
    ## $str$digits.d
    ## [1] 3
    ## 
    ## $str$vec.len
    ## [1] 4
    ## 
    ## $str$list.len
    ## [1] 99
    ## 
    ## $str$deparse.lines
    ## NULL
    ## 
    ## $str$drop.deparse.attr
    ## [1] TRUE
    ## 
    ## $str$formatNum
    ## function (x, ...) 
    ## format(x, trim = TRUE, drop0trailing = TRUE, ...)
    ## <environment: 0x00000280c94abdb8>
    ## 
    ## 
    ## $str.dendrogram.last
    ## [1] "`"
    ## 
    ## $tikzMetricsDictionary
    ## [1] "学习R-tikzDictionary"
    ## 
    ## $timeout
    ## [1] 60
    ## 
    ## $try.outFile
    ## A connection with                    
    ## description ""      
    ## class       "file"  
    ## mode        "w+b"   
    ## text        "binary"
    ## opened      "opened"
    ## can read    "yes"   
    ## can write   "yes"   
    ## 
    ## $ts.eps
    ## [1] 1e-05
    ## 
    ## $ts.S.compat
    ## [1] FALSE
    ## 
    ## $unzip
    ## [1] "internal"
    ## 
    ## $useFancyQuotes
    ## [1] FALSE
    ## 
    ## $verbose
    ## [1] FALSE
    ## 
    ## $warn
    ## [1] 0
    ## 
    ## $warning.length
    ## [1] 1000
    ## 
    ## $warnPartialMatchArgs
    ## [1] FALSE
    ## 
    ## $warnPartialMatchAttr
    ## [1] FALSE
    ## 
    ## $warnPartialMatchDollar
    ## [1] FALSE
    ## 
    ## $width
    ## [1] 80
    ## 
    ## $windowsTimeouts
    ## [1] 100 500

    # savehistory('filename.Rhistory')  # 将历史命令保存为文件夹内
    # loadhistory('history.Rhistory')  # 导入历史命令
    # save(object,file = filename.RData)  # 保存变量到指定工作映像文件内

    # load('filename.RData') 导入工作映像

    # source('a_script.R')  # 运行脚本

    # 储存变量,以便重复使用
    lmfit <- lm(mpg~wt,data=mtcars)  # 讲运算结果存在变量中
    summary(lmfit)  # 调用运算结果

    ## 
    ## Call:
    ## lm(formula = mpg ~ wt, data = mtcars)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -4.5432 -2.3647 -0.1252  1.4096  6.8727 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  37.2851     1.8776  19.858  < 2e-16 ***
    ## wt           -5.3445     0.5591  -9.559 1.29e-10 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 3.046 on 30 degrees of freedom
    ## Multiple R-squared:  0.7528, Adjusted R-squared:  0.7446 
    ## F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10

    # 设置镜像
    options(repos=c(CRAN="https://mirror.tuna.tsinghua.edu.cn/CRAN/"))

关于R包

    install.packages('packagesname')  # 安装R包

    ## Warning: package 'packagesname' is not available for this version of R
    ## 
    ## A version of this package for your version of R might be available elsewhere,
    ## see the ideas at
    ## https://cran.r-project.org/doc/manuals/r-patched/R-admin.html#Installing-packages

    # library('packagename')  # 导入R包

    # library()   # 显示库中有的包

    search() #  查看已加载的可用R包

    ## [1] ".GlobalEnv"        "package:stats"     "package:graphics" 
    ## [4] "package:grDevices" "package:utils"     "package:datasets" 
    ## [7] "package:methods"   "Autoloads"         "package:base"

    # .libPaths()  # 查看R包所在位置

    # update.packages('packagename') # 更新R包

    installed.packages() # 列出已安装的R包

    ##                      Package                LibPath              Version     
    ## abind                "abind"                "B:/R-4.5.1/library" "1.4-8"     
    ## askpass              "askpass"              "B:/R-4.5.1/library" "1.2.1"     
    ## backports            "backports"            "B:/R-4.5.1/library" "1.5.0"     
    ## base                 "base"                 "B:/R-4.5.1/library" "4.5.1"     
    ## base64enc            "base64enc"            "B:/R-4.5.1/library" "0.1-3"     
    ## BH                   "BH"                   "B:/R-4.5.1/library" "1.87.0-1"  
    ## Biobase              "Biobase"              "B:/R-4.5.1/library" "2.68.0"    
    ## BiocGenerics         "BiocGenerics"         "B:/R-4.5.1/library" "0.54.0"    
    ## BiocManager          "BiocManager"          "B:/R-4.5.1/library" "1.30.26"   
    ## BiocParallel         "BiocParallel"         "B:/R-4.5.1/library" "1.42.1"    
    ## BiocVersion          "BiocVersion"          "B:/R-4.5.1/library" "3.21.1"    
    ## bit                  "bit"                  "B:/R-4.5.1/library" "4.6.0"     
    ## bit64                "bit64"                "B:/R-4.5.1/library" "4.6.0-1"   
    ## boot                 "boot"                 "B:/R-4.5.1/library" "1.3-31"    
    ## broom                "broom"                "B:/R-4.5.1/library" "1.0.8"     
    ## bslib                "bslib"                "B:/R-4.5.1/library" "0.9.0"     
    ## cachem               "cachem"               "B:/R-4.5.1/library" "1.1.0"     
    ## car                  "car"                  "B:/R-4.5.1/library" "3.1-3"     
    ## carData              "carData"              "B:/R-4.5.1/library" "3.0-5"     
    ## caret                "caret"                "B:/R-4.5.1/library" "7.0-1"     
    ## cellranger           "cellranger"           "B:/R-4.5.1/library" "1.1.0"     
    ## class                "class"                "B:/R-4.5.1/library" "7.3-23"    
    ## cli                  "cli"                  "B:/R-4.5.1/library" "3.6.5"     
    ## clipr                "clipr"                "B:/R-4.5.1/library" "0.8.0"     
    ## clock                "clock"                "B:/R-4.5.1/library" "0.7.3"     
    ## cluster              "cluster"              "B:/R-4.5.1/library" "2.1.8.1"   
    ## codetools            "codetools"            "B:/R-4.5.1/library" "0.2-20"    
    ## colorspace           "colorspace"           "B:/R-4.5.1/library" "2.1-1"     
    ## colourpicker         "colourpicker"         "B:/R-4.5.1/library" "1.3.0"     
    ## commonmark           "commonmark"           "B:/R-4.5.1/library" "2.0.0"     
    ## compiler             "compiler"             "B:/R-4.5.1/library" "4.5.1"     
    ## corrplot             "corrplot"             "B:/R-4.5.1/library" "0.95"      
    ## cowplot              "cowplot"              "B:/R-4.5.1/library" "1.2.0"     
    ## cpp11                "cpp11"                "B:/R-4.5.1/library" "0.5.2"     
    ## crayon               "crayon"               "B:/R-4.5.1/library" "1.5.3"     
    ## curl                 "curl"                 "B:/R-4.5.1/library" "6.4.0"     
    ## data.table           "data.table"           "B:/R-4.5.1/library" "1.17.8"    
    ## datasets             "datasets"             "B:/R-4.5.1/library" "4.5.1"     
    ## DelayedArray         "DelayedArray"         "B:/R-4.5.1/library" "0.34.1"    
    ## Deriv                "Deriv"                "B:/R-4.5.1/library" "4.2.0"     
    ## DESeq2               "DESeq2"               "B:/R-4.5.1/library" "1.48.1"    
    ## diagram              "diagram"              "B:/R-4.5.1/library" "1.6.5"     
    ## digest               "digest"               "B:/R-4.5.1/library" "0.6.37"    
    ## doBy                 "doBy"                 "B:/R-4.5.1/library" "4.7.0"     
    ## dplyr                "dplyr"                "B:/R-4.5.1/library" "1.1.4"     
    ## dunn.test            "dunn.test"            "B:/R-4.5.1/library" "1.3.6"     
    ## e1071                "e1071"                "B:/R-4.5.1/library" "1.7-16"    
    ## emmeans              "emmeans"              "B:/R-4.5.1/library" "1.11.2"    
    ## EnhancedVolcano      "EnhancedVolcano"      "B:/R-4.5.1/library" "1.26.0"    
    ## estimability         "estimability"         "B:/R-4.5.1/library" "1.5.1"     
    ## evaluate             "evaluate"             "B:/R-4.5.1/library" "1.0.4"     
    ## farver               "farver"               "B:/R-4.5.1/library" "2.1.2"     
    ## fastmap              "fastmap"              "B:/R-4.5.1/library" "1.2.0"     
    ## FlexParamCurve       "FlexParamCurve"       "B:/R-4.5.1/library" "1.5-6"     
    ## fontawesome          "fontawesome"          "B:/R-4.5.1/library" "0.5.3"     
    ## forcats              "forcats"              "B:/R-4.5.1/library" "1.0.0"     
    ## foreach              "foreach"              "B:/R-4.5.1/library" "1.5.2"     
    ## foreign              "foreign"              "B:/R-4.5.1/library" "0.8-90"    
    ## formatR              "formatR"              "B:/R-4.5.1/library" "1.14"      
    ## Formula              "Formula"              "B:/R-4.5.1/library" "1.2-5"     
    ## fs                   "fs"                   "B:/R-4.5.1/library" "1.6.6"     
    ## FSA                  "FSA"                  "B:/R-4.5.1/library" "0.10.0"    
    ## futile.logger        "futile.logger"        "B:/R-4.5.1/library" "1.4.3"     
    ## futile.options       "futile.options"       "B:/R-4.5.1/library" "1.0.1"     
    ## future               "future"               "B:/R-4.5.1/library" "1.58.0"    
    ## future.apply         "future.apply"         "B:/R-4.5.1/library" "1.20.0"    
    ## generics             "generics"             "B:/R-4.5.1/library" "0.1.4"     
    ## GenomeInfoDb         "GenomeInfoDb"         "B:/R-4.5.1/library" "1.44.0"    
    ## GenomeInfoDbData     "GenomeInfoDbData"     "B:/R-4.5.1/library" "1.2.14"    
    ## GenomicRanges        "GenomicRanges"        "B:/R-4.5.1/library" "1.60.0"    
    ## ggcorrplot           "ggcorrplot"           "B:/R-4.5.1/library" "0.1.4.1"   
    ## ggExtra              "ggExtra"              "B:/R-4.5.1/library" "0.10.1"    
    ## ggplot2              "ggplot2"              "B:/R-4.5.1/library" "3.5.2"     
    ## ggpubr               "ggpubr"               "B:/R-4.5.1/library" "0.6.1"     
    ## ggrepel              "ggrepel"              "B:/R-4.5.1/library" "0.9.6"     
    ## ggsci                "ggsci"                "B:/R-4.5.1/library" "3.2.0"     
    ## ggsignif             "ggsignif"             "B:/R-4.5.1/library" "0.6.4"     
    ## glmnet               "glmnet"               "B:/R-4.5.1/library" "4.1-10"    
    ## globals              "globals"              "B:/R-4.5.1/library" "0.18.0"    
    ## glue                 "glue"                 "B:/R-4.5.1/library" "1.8.0"     
    ## gower                "gower"                "B:/R-4.5.1/library" "1.0.2"     
    ## graphics             "graphics"             "B:/R-4.5.1/library" "4.5.1"     
    ## grDevices            "grDevices"            "B:/R-4.5.1/library" "4.5.1"     
    ## grid                 "grid"                 "B:/R-4.5.1/library" "4.5.1"     
    ## gridExtra            "gridExtra"            "B:/R-4.5.1/library" "2.3"       
    ## gtable               "gtable"               "B:/R-4.5.1/library" "0.3.6"     
    ## hardhat              "hardhat"              "B:/R-4.5.1/library" "1.4.1"     
    ## haven                "haven"                "B:/R-4.5.1/library" "2.5.5"     
    ## highr                "highr"                "B:/R-4.5.1/library" "0.11"      
    ## hms                  "hms"                  "B:/R-4.5.1/library" "1.1.3"     
    ## htmltools            "htmltools"            "B:/R-4.5.1/library" "0.5.8.1"   
    ## htmlwidgets          "htmlwidgets"          "B:/R-4.5.1/library" "1.6.4"     
    ## httpuv               "httpuv"               "B:/R-4.5.1/library" "1.6.16"    
    ## httr                 "httr"                 "B:/R-4.5.1/library" "1.4.7"     
    ## ipred                "ipred"                "B:/R-4.5.1/library" "0.9-15"    
    ## IRanges              "IRanges"              "B:/R-4.5.1/library" "2.42.0"    
    ## isoband              "isoband"              "B:/R-4.5.1/library" "0.2.7"     
    ## iterators            "iterators"            "B:/R-4.5.1/library" "1.0.14"    
    ## jquerylib            "jquerylib"            "B:/R-4.5.1/library" "0.1.4"     
    ## jsonlite             "jsonlite"             "B:/R-4.5.1/library" "2.0.0"     
    ## KernSmooth           "KernSmooth"           "B:/R-4.5.1/library" "2.23-26"   
    ## knitr                "knitr"                "B:/R-4.5.1/library" "1.50"      
    ## labeling             "labeling"             "B:/R-4.5.1/library" "0.4.3"     
    ## lambda.r             "lambda.r"             "B:/R-4.5.1/library" "1.2.4"     
    ## later                "later"                "B:/R-4.5.1/library" "1.4.2"     
    ## lattice              "lattice"              "B:/R-4.5.1/library" "0.22-7"    
    ## lava                 "lava"                 "B:/R-4.5.1/library" "1.8.1"     
    ## lifecycle            "lifecycle"            "B:/R-4.5.1/library" "1.0.4"     
    ## listenv              "listenv"              "B:/R-4.5.1/library" "0.9.1"     
    ## lme4                 "lme4"                 "B:/R-4.5.1/library" "1.1-37"    
    ## lmtest               "lmtest"               "B:/R-4.5.1/library" "0.9-40"    
    ## locfit               "locfit"               "B:/R-4.5.1/library" "1.5-9.12"  
    ## lubridate            "lubridate"            "B:/R-4.5.1/library" "1.9.4"     
    ## magrittr             "magrittr"             "B:/R-4.5.1/library" "2.0.3"     
    ## MASS                 "MASS"                 "B:/R-4.5.1/library" "7.3-65"    
    ## Matrix               "Matrix"               "B:/R-4.5.1/library" "1.7-3"     
    ## MatrixGenerics       "MatrixGenerics"       "B:/R-4.5.1/library" "1.20.0"    
    ## MatrixModels         "MatrixModels"         "B:/R-4.5.1/library" "0.5-4"     
    ## matrixStats          "matrixStats"          "B:/R-4.5.1/library" "1.5.0"     
    ## memoise              "memoise"              "B:/R-4.5.1/library" "2.0.1"     
    ## methods              "methods"              "B:/R-4.5.1/library" "4.5.1"     
    ## mgcv                 "mgcv"                 "B:/R-4.5.1/library" "1.9-3"     
    ## microbenchmark       "microbenchmark"       "B:/R-4.5.1/library" "1.5.0"     
    ## mime                 "mime"                 "B:/R-4.5.1/library" "0.13"      
    ## miniUI               "miniUI"               "B:/R-4.5.1/library" "0.1.2"     
    ## minqa                "minqa"                "B:/R-4.5.1/library" "1.2.8"     
    ## ModelMetrics         "ModelMetrics"         "B:/R-4.5.1/library" "1.2.2.2"   
    ## modelr               "modelr"               "B:/R-4.5.1/library" "0.1.11"    
    ## moments              "moments"              "B:/R-4.5.1/library" "0.14.1"    
    ## mvtnorm              "mvtnorm"              "B:/R-4.5.1/library" "1.3-3"     
    ## nlme                 "nlme"                 "B:/R-4.5.1/library" "3.1-168"   
    ## nloptr               "nloptr"               "B:/R-4.5.1/library" "2.2.1"     
    ## nnet                 "nnet"                 "B:/R-4.5.1/library" "7.3-20"    
    ## numDeriv             "numDeriv"             "B:/R-4.5.1/library" "2016.8-1.1"
    ## openssl              "openssl"              "B:/R-4.5.1/library" "2.3.3"     
    ## parallel             "parallel"             "B:/R-4.5.1/library" "4.5.1"     
    ## parallelly           "parallelly"           "B:/R-4.5.1/library" "1.45.0"    
    ## patchwork            "patchwork"            "B:/R-4.5.1/library" "1.3.1"     
    ## pbkrtest             "pbkrtest"             "B:/R-4.5.1/library" "0.5.5"     
    ## pillar               "pillar"               "B:/R-4.5.1/library" "1.11.0"    
    ## pkgconfig            "pkgconfig"            "B:/R-4.5.1/library" "2.0.3"     
    ## plotrix              "plotrix"              "B:/R-4.5.1/library" "3.8-4"     
    ## plyr                 "plyr"                 "B:/R-4.5.1/library" "1.8.9"     
    ## polynom              "polynom"              "B:/R-4.5.1/library" "1.4-1"     
    ## ppcor                "ppcor"                "B:/R-4.5.1/library" "1.1"       
    ## prettyunits          "prettyunits"          "B:/R-4.5.1/library" "1.2.0"     
    ## pROC                 "pROC"                 "B:/R-4.5.1/library" "1.18.5"    
    ## processx             "processx"             "B:/R-4.5.1/library" "3.8.6"     
    ## prodlim              "prodlim"              "B:/R-4.5.1/library" "2025.04.28"
    ## progress             "progress"             "B:/R-4.5.1/library" "1.2.3"     
    ## progressr            "progressr"            "B:/R-4.5.1/library" "0.15.1"    
    ## promises             "promises"             "B:/R-4.5.1/library" "1.3.3"     
    ## proxy                "proxy"                "B:/R-4.5.1/library" "0.4-27"    
    ## ps                   "ps"                   "B:/R-4.5.1/library" "1.9.1"     
    ## purrr                "purrr"                "B:/R-4.5.1/library" "1.1.0"     
    ## quantreg             "quantreg"             "B:/R-4.5.1/library" "6.1"       
    ## quarto               "quarto"               "B:/R-4.5.1/library" "1.5.0"     
    ## R.methodsS3          "R.methodsS3"          "B:/R-4.5.1/library" "1.8.2"     
    ## R.oo                 "R.oo"                 "B:/R-4.5.1/library" "1.27.1"    
    ## R.utils              "R.utils"              "B:/R-4.5.1/library" "2.13.0"    
    ## R6                   "R6"                   "B:/R-4.5.1/library" "2.6.1"     
    ## rappdirs             "rappdirs"             "B:/R-4.5.1/library" "0.3.3"     
    ## rbibutils            "rbibutils"            "B:/R-4.5.1/library" "2.3"       
    ## RColorBrewer         "RColorBrewer"         "B:/R-4.5.1/library" "1.1-3"     
    ## Rcpp                 "Rcpp"                 "B:/R-4.5.1/library" "1.1.0"     
    ## RcppArmadillo        "RcppArmadillo"        "B:/R-4.5.1/library" "14.6.0-1"  
    ## RcppEigen            "RcppEigen"            "B:/R-4.5.1/library" "0.3.4.0.2" 
    ## Rdpack               "Rdpack"               "B:/R-4.5.1/library" "2.6.4"     
    ## readr                "readr"                "B:/R-4.5.1/library" "2.1.5"     
    ## readxl               "readxl"               "B:/R-4.5.1/library" "1.4.5"     
    ## recipes              "recipes"              "B:/R-4.5.1/library" "1.3.1"     
    ## reformulas           "reformulas"           "B:/R-4.5.1/library" "0.4.1"     
    ## rematch              "rematch"              "B:/R-4.5.1/library" "2.0.0"     
    ## reshape2             "reshape2"             "B:/R-4.5.1/library" "1.4.4"     
    ## rio                  "rio"                  "B:/R-4.5.1/library" "1.2.3"     
    ## rlang                "rlang"                "B:/R-4.5.1/library" "1.1.6"     
    ## rmarkdown            "rmarkdown"            "B:/R-4.5.1/library" "2.29"      
    ## rpart                "rpart"                "B:/R-4.5.1/library" "4.1.24"    
    ## rstatix              "rstatix"              "B:/R-4.5.1/library" "0.7.2"     
    ## rstudioapi           "rstudioapi"           "B:/R-4.5.1/library" "0.17.1"    
    ## S4Arrays             "S4Arrays"             "B:/R-4.5.1/library" "1.8.1"     
    ## S4Vectors            "S4Vectors"            "B:/R-4.5.1/library" "0.46.0"    
    ## sass                 "sass"                 "B:/R-4.5.1/library" "0.4.10"    
    ## scales               "scales"               "B:/R-4.5.1/library" "1.4.0"     
    ## shape                "shape"                "B:/R-4.5.1/library" "1.4.6.1"   
    ## shiny                "shiny"                "B:/R-4.5.1/library" "1.11.1"    
    ## shinyjs              "shinyjs"              "B:/R-4.5.1/library" "2.1.0"     
    ## snow                 "snow"                 "B:/R-4.5.1/library" "0.4-4"     
    ## sourcetools          "sourcetools"          "B:/R-4.5.1/library" "0.1.7-1"   
    ## SparseArray          "SparseArray"          "B:/R-4.5.1/library" "1.8.0"     
    ## SparseM              "SparseM"              "B:/R-4.5.1/library" "1.84-2"    
    ## sparsevctrs          "sparsevctrs"          "B:/R-4.5.1/library" "0.3.4"     
    ## spatial              "spatial"              "B:/R-4.5.1/library" "7.3-18"    
    ## splines              "splines"              "B:/R-4.5.1/library" "4.5.1"     
    ## SQUAREM              "SQUAREM"              "B:/R-4.5.1/library" "2021.1"    
    ## stats                "stats"                "B:/R-4.5.1/library" "4.5.1"     
    ## stats4               "stats4"               "B:/R-4.5.1/library" "4.5.1"     
    ## stringi              "stringi"              "B:/R-4.5.1/library" "1.8.7"     
    ## stringr              "stringr"              "B:/R-4.5.1/library" "1.5.1"     
    ## SummarizedExperiment "SummarizedExperiment" "B:/R-4.5.1/library" "1.38.1"    
    ## survival             "survival"             "B:/R-4.5.1/library" "3.8-3"     
    ## sys                  "sys"                  "B:/R-4.5.1/library" "3.4.3"     
    ## tcltk                "tcltk"                "B:/R-4.5.1/library" "4.5.1"     
    ## tibble               "tibble"               "B:/R-4.5.1/library" "3.3.0"     
    ## tidyr                "tidyr"                "B:/R-4.5.1/library" "1.3.1"     
    ## tidyselect           "tidyselect"           "B:/R-4.5.1/library" "1.2.1"     
    ## timechange           "timechange"           "B:/R-4.5.1/library" "0.3.0"     
    ## timeDate             "timeDate"             "B:/R-4.5.1/library" "4041.110"  
    ## tinytex              "tinytex"              "B:/R-4.5.1/library" "0.57"      
    ## titanic              "titanic"              "B:/R-4.5.1/library" "0.1.0"     
    ## tools                "tools"                "B:/R-4.5.1/library" "4.5.1"     
    ## translations         "translations"         "B:/R-4.5.1/library" "4.5.1"     
    ## tzdb                 "tzdb"                 "B:/R-4.5.1/library" "0.5.0"     
    ## UCSC.utils           "UCSC.utils"           "B:/R-4.5.1/library" "1.4.0"     
    ## utf8                 "utf8"                 "B:/R-4.5.1/library" "1.2.6"     
    ## utils                "utils"                "B:/R-4.5.1/library" "4.5.1"     
    ## vcd                  "vcd"                  "B:/R-4.5.1/library" "1.4-13"    
    ## vctrs                "vctrs"                "B:/R-4.5.1/library" "0.6.5"     
    ## viridisLite          "viridisLite"          "B:/R-4.5.1/library" "0.4.2"     
    ## vroom                "vroom"                "B:/R-4.5.1/library" "1.6.5"     
    ## withr                "withr"                "B:/R-4.5.1/library" "3.0.2"     
    ## writexl              "writexl"              "B:/R-4.5.1/library" "1.5.4"     
    ## xfun                 "xfun"                 "B:/R-4.5.1/library" "0.52"      
    ## xtable               "xtable"               "B:/R-4.5.1/library" "1.8-4"     
    ## XVector              "XVector"              "B:/R-4.5.1/library" "0.48.0"    
    ## yaml                 "yaml"                 "B:/R-4.5.1/library" "2.3.10"    
    ## zoo                  "zoo"                  "B:/R-4.5.1/library" "1.8-14"    
    ##                      Priority     
    ## abind                NA           
    ## askpass              NA           
    ## backports            NA           
    ## base                 "base"       
    ## base64enc            NA           
    ## BH                   NA           
    ## Biobase              NA           
    ## BiocGenerics         NA           
    ## BiocManager          NA           
    ## BiocParallel         NA           
    ## BiocVersion          NA           
    ## bit                  NA           
    ## bit64                NA           
    ## boot                 "recommended"
    ## broom                NA           
    ## bslib                NA           
    ## cachem               NA           
    ## car                  NA           
    ## carData              NA           
    ## caret                NA           
    ## cellranger           NA           
    ## class                "recommended"
    ## cli                  NA           
    ## clipr                NA           
    ## clock                NA           
    ## cluster              "recommended"
    ## codetools            "recommended"
    ## colorspace           NA           
    ## colourpicker         NA           
    ## commonmark           NA           
    ## compiler             "base"       
    ## corrplot             NA           
    ## cowplot              NA           
    ## cpp11                NA           
    ## crayon               NA           
    ## curl                 NA           
    ## data.table           NA           
    ## datasets             "base"       
    ## DelayedArray         NA           
    ## Deriv                NA           
    ## DESeq2               NA           
    ## diagram              NA           
    ## digest               NA           
    ## doBy                 NA           
    ## dplyr                NA           
    ## dunn.test            NA           
    ## e1071                NA           
    ## emmeans              NA           
    ## EnhancedVolcano      NA           
    ## estimability         NA           
    ## evaluate             NA           
    ## farver               NA           
    ## fastmap              NA           
    ## FlexParamCurve       NA           
    ## fontawesome          NA           
    ## forcats              NA           
    ## foreach              NA           
    ## foreign              "recommended"
    ## formatR              NA           
    ## Formula              NA           
    ## fs                   NA           
    ## FSA                  NA           
    ## futile.logger        NA           
    ## futile.options       NA           
    ## future               NA           
    ## future.apply         NA           
    ## generics             NA           
    ## GenomeInfoDb         NA           
    ## GenomeInfoDbData     NA           
    ## GenomicRanges        NA           
    ## ggcorrplot           NA           
    ## ggExtra              NA           
    ## ggplot2              NA           
    ## ggpubr               NA           
    ## ggrepel              NA           
    ## ggsci                NA           
    ## ggsignif             NA           
    ## glmnet               NA           
    ## globals              NA           
    ## glue                 NA           
    ## gower                NA           
    ## graphics             "base"       
    ## grDevices            "base"       
    ## grid                 "base"       
    ## gridExtra            NA           
    ## gtable               NA           
    ## hardhat              NA           
    ## haven                NA           
    ## highr                NA           
    ## hms                  NA           
    ## htmltools            NA           
    ## htmlwidgets          NA           
    ## httpuv               NA           
    ## httr                 NA           
    ## ipred                NA           
    ## IRanges              NA           
    ## isoband              NA           
    ## iterators            NA           
    ## jquerylib            NA           
    ## jsonlite             NA           
    ## KernSmooth           "recommended"
    ## knitr                NA           
    ## labeling             NA           
    ## lambda.r             NA           
    ## later                NA           
    ## lattice              "recommended"
    ## lava                 NA           
    ## lifecycle            NA           
    ## listenv              NA           
    ## lme4                 NA           
    ## lmtest               NA           
    ## locfit               NA           
    ## lubridate            NA           
    ## magrittr             NA           
    ## MASS                 "recommended"
    ## Matrix               "recommended"
    ## MatrixGenerics       NA           
    ## MatrixModels         NA           
    ## matrixStats          NA           
    ## memoise              NA           
    ## methods              "base"       
    ## mgcv                 "recommended"
    ## microbenchmark       NA           
    ## mime                 NA           
    ## miniUI               NA           
    ## minqa                NA           
    ## ModelMetrics         NA           
    ## modelr               NA           
    ## moments              NA           
    ## mvtnorm              NA           
    ## nlme                 "recommended"
    ## nloptr               NA           
    ## nnet                 "recommended"
    ## numDeriv             NA           
    ## openssl              NA           
    ## parallel             "base"       
    ## parallelly           NA           
    ## patchwork            NA           
    ## pbkrtest             NA           
    ## pillar               NA           
    ## pkgconfig            NA           
    ## plotrix              NA           
    ## plyr                 NA           
    ## polynom              NA           
    ## ppcor                NA           
    ## prettyunits          NA           
    ## pROC                 NA           
    ## processx             NA           
    ## prodlim              NA           
    ## progress             NA           
    ## progressr            NA           
    ## promises             NA           
    ## proxy                NA           
    ## ps                   NA           
    ## purrr                NA           
    ## quantreg             NA           
    ## quarto               NA           
    ## R.methodsS3          NA           
    ## R.oo                 NA           
    ## R.utils              NA           
    ## R6                   NA           
    ## rappdirs             NA           
    ## rbibutils            NA           
    ## RColorBrewer         NA           
    ## Rcpp                 NA           
    ## RcppArmadillo        NA           
    ## RcppEigen            NA           
    ## Rdpack               NA           
    ## readr                NA           
    ## readxl               NA           
    ## recipes              NA           
    ## reformulas           NA           
    ## rematch              NA           
    ## reshape2             NA           
    ## rio                  NA           
    ## rlang                NA           
    ## rmarkdown            NA           
    ## rpart                "recommended"
    ## rstatix              NA           
    ## rstudioapi           NA           
    ## S4Arrays             NA           
    ## S4Vectors            NA           
    ## sass                 NA           
    ## scales               NA           
    ## shape                NA           
    ## shiny                NA           
    ## shinyjs              NA           
    ## snow                 NA           
    ## sourcetools          NA           
    ## SparseArray          NA           
    ## SparseM              NA           
    ## sparsevctrs          NA           
    ## spatial              "recommended"
    ## splines              "base"       
    ## SQUAREM              NA           
    ## stats                "base"       
    ## stats4               "base"       
    ## stringi              NA           
    ## stringr              NA           
    ## SummarizedExperiment NA           
    ## survival             "recommended"
    ## sys                  NA           
    ## tcltk                "base"       
    ## tibble               NA           
    ## tidyr                NA           
    ## tidyselect           NA           
    ## timechange           NA           
    ## timeDate             NA           
    ## tinytex              NA           
    ## titanic              NA           
    ## tools                "base"       
    ## translations         NA           
    ## tzdb                 NA           
    ## UCSC.utils           NA           
    ## utf8                 NA           
    ## utils                "base"       
    ## vcd                  NA           
    ## vctrs                NA           
    ## viridisLite          NA           
    ## vroom                NA           
    ## withr                NA           
    ## writexl              NA           
    ## xfun                 NA           
    ## xtable               NA           
    ## XVector              NA           
    ## yaml                 NA           
    ## zoo                  NA           
    ##                      Depends                                                                                                                                                                                 
    ## abind                "R (>= 1.5.0)"                                                                                                                                                                          
    ## askpass              NA                                                                                                                                                                                      
    ## backports            "R (>= 3.0.0)"                                                                                                                                                                          
    ## base                 NA                                                                                                                                                                                      
    ## base64enc            "R (>= 2.9.0)"                                                                                                                                                                          
    ## BH                   NA                                                                                                                                                                                      
    ## Biobase              "R (>= 2.10), BiocGenerics (>= 0.27.1), utils"                                                                                                                                          
    ## BiocGenerics         "R (>= 4.0.0), methods, utils, graphics, stats, generics"                                                                                                                               
    ## BiocManager          NA                                                                                                                                                                                      
    ## BiocParallel         "methods, R (>= 4.1.0)"                                                                                                                                                                 
    ## BiocVersion          "R (>= 4.5.0)"                                                                                                                                                                          
    ## bit                  "R (>= 3.4.0)"                                                                                                                                                                          
    ## bit64                "R (>= 3.4.0), bit (>= 4.0.0)"                                                                                                                                                          
    ## boot                 "R (>= 3.0.0), graphics, stats"                                                                                                                                                         
    ## broom                "R (>= 3.5)"                                                                                                                                                                            
    ## bslib                "R (>= 2.10)"                                                                                                                                                                           
    ## cachem               NA                                                                                                                                                                                      
    ## car                  "R (>= 3.5.0), carData (>= 3.0-0)"                                                                                                                                                      
    ## carData              "R (>= 3.5.0)"                                                                                                                                                                          
    ## caret                "ggplot2, lattice (>= 0.20), R (>= 3.2.0)"                                                                                                                                              
    ## cellranger           "R (>= 3.0.0)"                                                                                                                                                                          
    ## class                "R (>= 3.0.0), stats, utils"                                                                                                                                                            
    ## cli                  "R (>= 3.4)"                                                                                                                                                                            
    ## clipr                NA                                                                                                                                                                                      
    ## clock                "R (>= 4.0.0)"                                                                                                                                                                          
    ## cluster              "R (>= 3.5.0)"                                                                                                                                                                          
    ## codetools            "R (>= 2.1)"                                                                                                                                                                            
    ## colorspace           "R (>= 3.0.0), methods"                                                                                                                                                                 
    ## colourpicker         "R (>= 3.1.0)"                                                                                                                                                                          
    ## commonmark           NA                                                                                                                                                                                      
    ## compiler             NA                                                                                                                                                                                      
    ## corrplot             NA                                                                                                                                                                                      
    ## cowplot              "R (>= 3.5.0)"                                                                                                                                                                          
    ## cpp11                "R (>= 4.0.0)"                                                                                                                                                                          
    ## crayon               NA                                                                                                                                                                                      
    ## curl                 "R (>= 3.0.0)"                                                                                                                                                                          
    ## data.table           "R (>= 3.3.0)"                                                                                                                                                                          
    ## datasets             NA                                                                                                                                                                                      
    ## DelayedArray         "R (>= 4.0.0), methods, stats4, Matrix, BiocGenerics (>=\n0.53.3), MatrixGenerics (>= 1.1.3), S4Vectors (>= 0.27.2),\nIRanges (>= 2.17.3), S4Arrays (>= 1.5.4), SparseArray (>=\n1.7.5)"
    ## Deriv                NA                                                                                                                                                                                      
    ## DESeq2               "S4Vectors (>= 0.23.18), IRanges, GenomicRanges,\nSummarizedExperiment (>= 1.1.6)"                                                                                                      
    ## diagram              "R (>= 2.01), shape"                                                                                                                                                                    
    ## digest               "R (>= 3.3.0)"                                                                                                                                                                          
    ## doBy                 "R (>= 4.2.0), methods"                                                                                                                                                                 
    ## dplyr                "R (>= 3.5.0)"                                                                                                                                                                          
    ## dunn.test            NA                                                                                                                                                                                      
    ## e1071                NA                                                                                                                                                                                      
    ## emmeans              "R (>= 4.1.0)"                                                                                                                                                                          
    ## EnhancedVolcano      "ggplot2, ggrepel"                                                                                                                                                                      
    ## estimability         "stats, R(>= 4.1.0)"                                                                                                                                                                    
    ## evaluate             "R (>= 3.6.0)"                                                                                                                                                                          
    ## farver               NA                                                                                                                                                                                      
    ## fastmap              NA                                                                                                                                                                                      
    ## FlexParamCurve       "nlme"                                                                                                                                                                                  
    ## fontawesome          "R (>= 3.3.0)"                                                                                                                                                                          
    ## forcats              "R (>= 3.4)"                                                                                                                                                                            
    ## foreach              "R (>= 2.5.0)"                                                                                                                                                                          
    ## foreign              "R (>= 4.0.0)"                                                                                                                                                                          
    ## formatR              "R (>= 3.2.3)"                                                                                                                                                                          
    ## Formula              "R (>= 2.0.0), stats"                                                                                                                                                                   
    ## fs                   "R (>= 3.6)"                                                                                                                                                                            
    ## FSA                  "R (>= 3.5.0)"                                                                                                                                                                          
    ## futile.logger        "R (>= 3.0.0)"                                                                                                                                                                          
    ## futile.options       "R (>= 2.8.0)"                                                                                                                                                                          
    ## future               "R (>= 3.2.0)"                                                                                                                                                                          
    ## future.apply         "R (>= 3.2.0), future (>= 1.49.0)"                                                                                                                                                      
    ## generics             "R (>= 3.6)"                                                                                                                                                                            
    ## GenomeInfoDb         "R (>= 4.0.0), methods, BiocGenerics (>= 0.53.2), S4Vectors (>=\n0.45.2), IRanges (>= 2.41.1)"                                                                                          
    ## GenomeInfoDbData     "R (>= 3.5.0)"                                                                                                                                                                          
    ## GenomicRanges        "R (>= 4.0.0), methods, stats4, BiocGenerics (>= 0.53.2),\nS4Vectors (>= 0.45.2), IRanges (>= 2.41.1), GenomeInfoDb (>=\n1.43.1)"                                                       
    ## ggcorrplot           "R (>= 3.3), ggplot2 (>= 3.3.6)"                                                                                                                                                        
    ## ggExtra              "R (>= 3.1.0)"                                                                                                                                                                          
    ## ggplot2              "R (>= 3.5)"                                                                                                                                                                            
    ## ggpubr               "R (>= 3.1.0), ggplot2 (>= 3.5.2)"                                                                                                                                                      
    ## ggrepel              "R (>= 3.0.0), ggplot2 (>= 2.2.0)"                                                                                                                                                      
    ## ggsci                "R (>= 3.5.0)"                                                                                                                                                                          
    ## ggsignif             NA                                                                                                                                                                                      
    ## glmnet               "R (>= 3.6.0), Matrix (>= 1.0-6)"                                                                                                                                                       
    ## globals              "R (>= 3.1.2)"                                                                                                                                                                          
    ## glue                 "R (>= 3.6)"                                                                                                                                                                            
    ## gower                NA                                                                                                                                                                                      
    ## graphics             NA                                                                                                                                                                                      
    ## grDevices            NA                                                                                                                                                                                      
    ## grid                 NA                                                                                                                                                                                      
    ## gridExtra            NA                                                                                                                                                                                      
    ## gtable               "R (>= 4.0)"                                                                                                                                                                            
    ## hardhat              "R (>= 3.5.0)"                                                                                                                                                                          
    ## haven                "R (>= 3.6)"                                                                                                                                                                            
    ## highr                "R (>= 3.3.0)"                                                                                                                                                                          
    ## hms                  NA                                                                                                                                                                                      
    ## htmltools            "R (>= 2.14.1)"                                                                                                                                                                         
    ## htmlwidgets          NA                                                                                                                                                                                      
    ## httpuv               "R (>= 2.15.1)"                                                                                                                                                                         
    ## httr                 "R (>= 3.5)"                                                                                                                                                                            
    ## ipred                "R (>= 2.10)"                                                                                                                                                                           
    ## IRanges              "R (>= 4.0.0), methods, utils, stats, BiocGenerics (>= 0.53.2),\nS4Vectors (>= 0.45.4)"                                                                                                 
    ## isoband              NA                                                                                                                                                                                      
    ## iterators            "R (>= 2.5.0), utils"                                                                                                                                                                   
    ## jquerylib            NA                                                                                                                                                                                      
    ## jsonlite             "methods"                                                                                                                                                                               
    ## KernSmooth           "R (>= 2.5.0), stats"                                                                                                                                                                   
    ## knitr                "R (>= 3.6.0)"                                                                                                                                                                          
    ## labeling             NA                                                                                                                                                                                      
    ## lambda.r             "R (>= 3.0.0)"                                                                                                                                                                          
    ## later                NA                                                                                                                                                                                      
    ## lattice              "R (>= 4.0.0)"                                                                                                                                                                          
    ## lava                 "R (>= 3.0)"                                                                                                                                                                            
    ## lifecycle            "R (>= 3.6)"                                                                                                                                                                            
    ## listenv              "R (>= 3.1.2)"                                                                                                                                                                          
    ## lme4                 "R (>= 3.6.0), Matrix, methods, stats"                                                                                                                                                  
    ## lmtest               "R (>= 3.0.0), stats, zoo"                                                                                                                                                              
    ## locfit               "R (>= 4.1.0)"                                                                                                                                                                          
    ## lubridate            "methods, R (>= 3.2)"                                                                                                                                                                   
    ## magrittr             "R (>= 3.4.0)"                                                                                                                                                                          
    ## MASS                 "R (>= 4.4.0), grDevices, graphics, stats, utils"                                                                                                                                       
    ## Matrix               "R (>= 4.4), methods"                                                                                                                                                                   
    ## MatrixGenerics       "matrixStats (>= 1.4.1)"                                                                                                                                                                
    ## MatrixModels         "R (>= 3.6.0)"                                                                                                                                                                          
    ## matrixStats          "R (>= 3.4.0)"                                                                                                                                                                          
    ## memoise              NA                                                                                                                                                                                      
    ## methods              NA                                                                                                                                                                                      
    ## mgcv                 "R (>= 3.6.0), nlme (>= 3.1-64)"                                                                                                                                                        
    ## microbenchmark       "R (>= 3.2.0)"                                                                                                                                                                          
    ## mime                 NA                                                                                                                                                                                      
    ## miniUI               NA                                                                                                                                                                                      
    ## minqa                NA                                                                                                                                                                                      
    ## ModelMetrics         "R (>= 3.2.2)"                                                                                                                                                                          
    ## modelr               "R (>= 3.2)"                                                                                                                                                                            
    ## moments              NA                                                                                                                                                                                      
    ## mvtnorm              "R(>= 3.5.0)"                                                                                                                                                                           
    ## nlme                 "R (>= 3.6.0)"                                                                                                                                                                          
    ## nloptr               NA                                                                                                                                                                                      
    ## nnet                 "R (>= 3.0.0), stats, utils"                                                                                                                                                            
    ## numDeriv             "R (>= 2.11.1)"                                                                                                                                                                         
    ## openssl              NA                                                                                                                                                                                      
    ## parallel             NA                                                                                                                                                                                      
    ## parallelly           NA                                                                                                                                                                                      
    ## patchwork            NA                                                                                                                                                                                      
    ## pbkrtest             "R (>= 4.2.0), lme4 (>= 1.1.31)"                                                                                                                                                        
    ## pillar               NA                                                                                                                                                                                      
    ## pkgconfig            NA                                                                                                                                                                                      
    ## plotrix              "R (>= 3.5.0)"                                                                                                                                                                          
    ## plyr                 "R (>= 3.1.0)"                                                                                                                                                                          
    ## polynom              NA                                                                                                                                                                                      
    ## ppcor                "R (>= 2.6.0), MASS"                                                                                                                                                                    
    ## prettyunits          "R(>= 2.10)"                                                                                                                                                                            
    ## pROC                 "R (>= 2.14)"                                                                                                                                                                           
    ## processx             "R (>= 3.4.0)"                                                                                                                                                                          
    ## prodlim              "R (>= 4.1.0)"                                                                                                                                                                          
    ## progress             "R (>= 3.6)"                                                                                                                                                                            
    ## progressr            "R (>= 3.5.0)"                                                                                                                                                                          
    ## promises             NA                                                                                                                                                                                      
    ## proxy                "R (>= 3.4.0)"                                                                                                                                                                          
    ## ps                   "R (>= 3.4)"                                                                                                                                                                            
    ## purrr                "R (>= 4.1)"                                                                                                                                                                            
    ## quantreg             "R (>= 3.5), stats, SparseM"                                                                                                                                                            
    ## quarto               "R (>= 4.1.0)"                                                                                                                                                                          
    ## R.methodsS3          "R (>= 2.13.0)"                                                                                                                                                                         
    ## R.oo                 "R (>= 2.13.0), R.methodsS3 (>= 1.8.2)"                                                                                                                                                 
    ## R.utils              "R (>= 2.14.0), R.oo"                                                                                                                                                                   
    ## R6                   "R (>= 3.6)"                                                                                                                                                                            
    ## rappdirs             "R (>= 3.2)"                                                                                                                                                                            
    ## rbibutils            "R (>= 2.10)"                                                                                                                                                                           
    ## RColorBrewer         "R (>= 2.0.0)"                                                                                                                                                                          
    ## Rcpp                 NA                                                                                                                                                                                      
    ## RcppArmadillo        "R (>= 3.3.0)"                                                                                                                                                                          
    ## RcppEigen            "R (>= 3.6.0)"                                                                                                                                                                          
    ## Rdpack               "R (>= 2.15.0), methods"                                                                                                                                                                
    ## readr                "R (>= 3.6)"                                                                                                                                                                            
    ## readxl               "R (>= 3.6)"                                                                                                                                                                            
    ## recipes              "dplyr (>= 1.1.0), R (>= 4.1)"                                                                                                                                                          
    ## reformulas           NA                                                                                                                                                                                      
    ## rematch              NA                                                                                                                                                                                      
    ## reshape2             "R (>= 3.1)"                                                                                                                                                                            
    ## rio                  "R (>= 4.0)"                                                                                                                                                                            
    ## rlang                "R (>= 3.5.0)"                                                                                                                                                                          
    ## rmarkdown            "R (>= 3.0)"                                                                                                                                                                            
    ## rpart                "R (>= 2.15.0), graphics, stats, grDevices"                                                                                                                                             
    ## rstatix              "R (>= 3.3.0)"                                                                                                                                                                          
    ## rstudioapi           NA                                                                                                                                                                                      
    ## S4Arrays             "R (>= 4.3.0), methods, Matrix, abind, BiocGenerics (>=\n0.45.2), S4Vectors, IRanges"                                                                                                   
    ## S4Vectors            "R (>= 4.0.0), methods, utils, stats, stats4, BiocGenerics (>=\n0.53.2)"                                                                                                                
    ## sass                 NA                                                                                                                                                                                      
    ## scales               "R (>= 4.1)"                                                                                                                                                                            
    ## shape                "R (>= 2.01)"                                                                                                                                                                           
    ## shiny                "R (>= 3.0.2), methods"                                                                                                                                                                 
    ## shinyjs              "R (>= 3.1.0)"                                                                                                                                                                          
    ## snow                 "R (>= 2.13.1), utils"                                                                                                                                                                  
    ## sourcetools          "R (>= 3.0.2)"                                                                                                                                                                          
    ## SparseArray          "R (>= 4.3.0), methods, Matrix, BiocGenerics (>= 0.43.1),\nMatrixGenerics (>= 1.11.1), S4Vectors (>= 0.43.2), S4Arrays (>=\n1.5.11)"                                                    
    ## SparseM              "R (>= 2.15), methods"                                                                                                                                                                  
    ## sparsevctrs          "R (>= 4.1)"                                                                                                                                                                            
    ## spatial              "R (>= 3.0.0), graphics, stats, utils"                                                                                                                                                  
    ## splines              NA                                                                                                                                                                                      
    ## SQUAREM              "R (>= 3.0)"                                                                                                                                                                            
    ## stats                NA                                                                                                                                                                                      
    ## stats4               NA                                                                                                                                                                                      
    ## stringi              "R (>= 3.4)"                                                                                                                                                                            
    ## stringr              "R (>= 3.6)"                                                                                                                                                                            
    ## SummarizedExperiment "R (>= 4.0.0), methods, MatrixGenerics (>= 1.1.3),\nGenomicRanges (>= 1.55.2), Biobase"                                                                                                 
    ## survival             "R (>= 3.5.0)"                                                                                                                                                                          
    ## sys                  NA                                                                                                                                                                                      
    ## tcltk                NA                                                                                                                                                                                      
    ## tibble               "R (>= 3.4.0)"                                                                                                                                                                          
    ## tidyr                "R (>= 3.6)"                                                                                                                                                                            
    ## tidyselect           "R (>= 3.4)"                                                                                                                                                                            
    ## timechange           "R (>= 3.3)"                                                                                                                                                                            
    ## timeDate             "R (>= 3.6.0), methods"                                                                                                                                                                 
    ## tinytex              NA                                                                                                                                                                                      
    ## titanic              "R (>= 3.1.2)"                                                                                                                                                                          
    ## tools                NA                                                                                                                                                                                      
    ## translations         NA                                                                                                                                                                                      
    ## tzdb                 "R (>= 4.0.0)"                                                                                                                                                                          
    ## UCSC.utils           NA                                                                                                                                                                                      
    ## utf8                 "R (>= 2.10)"                                                                                                                                                                           
    ## utils                NA                                                                                                                                                                                      
    ## vcd                  "R (>= 2.4.0), grid"                                                                                                                                                                    
    ## vctrs                "R (>= 3.5.0)"                                                                                                                                                                          
    ## viridisLite          "R (>= 2.10)"                                                                                                                                                                           
    ## vroom                "R (>= 3.6)"                                                                                                                                                                            
    ## withr                "R (>= 3.6.0)"                                                                                                                                                                          
    ## writexl              NA                                                                                                                                                                                      
    ## xfun                 "R (>= 3.2.0)"                                                                                                                                                                          
    ## xtable               "R (>= 2.10.0)"                                                                                                                                                                         
    ## XVector              "R (>= 4.0.0), methods, BiocGenerics (>= 0.37.0), S4Vectors (>=\n0.27.12), IRanges (>= 2.23.9)"                                                                                         
    ## yaml                 NA                                                                                                                                                                                      
    ## zoo                  "R (>= 3.1.0), stats"                                                                                                                                                                   
    ##                      Imports                                                                                                                                                                                                                                                                                                                                                          
    ## abind                "methods, utils"                                                                                                                                                                                                                                                                                                                                                 
    ## askpass              "sys (>= 2.1)"                                                                                                                                                                                                                                                                                                                                                   
    ## backports            NA                                                                                                                                                                                                                                                                                                                                                               
    ## base                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## base64enc            NA                                                                                                                                                                                                                                                                                                                                                               
    ## BH                   NA                                                                                                                                                                                                                                                                                                                                                               
    ## Biobase              "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## BiocGenerics         "methods, utils, graphics, stats"                                                                                                                                                                                                                                                                                                                                
    ## BiocManager          "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## BiocParallel         "stats, utils, futile.logger, parallel, snow, codetools"                                                                                                                                                                                                                                                                                                         
    ## BiocVersion          NA                                                                                                                                                                                                                                                                                                                                                               
    ## bit                  NA                                                                                                                                                                                                                                                                                                                                                               
    ## bit64                "graphics, methods, stats, utils"                                                                                                                                                                                                                                                                                                                                
    ## boot                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## broom                "backports, cli, dplyr (>= 1.0.0), generics (>= 0.0.2), glue,\nlifecycle, purrr, rlang (>= 1.1.0), stringr, tibble (>= 3.0.0),\ntidyr (>= 1.0.0)"                                                                                                                                                                                                                
    ## bslib                "base64enc, cachem, fastmap (>= 1.1.1), grDevices, htmltools\n(>= 0.5.8), jquerylib (>= 0.1.3), jsonlite, lifecycle, memoise\n(>= 2.0.1), mime, rlang, sass (>= 0.4.9)"                                                                                                                                                                                          
    ## cachem               "rlang, fastmap (>= 1.2.0)"                                                                                                                                                                                                                                                                                                                                      
    ## car                  "abind, Formula, MASS, mgcv, nnet, pbkrtest (>= 0.4-4),\nquantreg, grDevices, utils, stats, graphics, lme4 (>=\n1.1-27.1), nlme, scales"                                                                                                                                                                                                                         
    ## carData              NA                                                                                                                                                                                                                                                                                                                                                               
    ## caret                "e1071, foreach, grDevices, methods, ModelMetrics (>= 1.2.2.2),\nnlme, plyr, pROC, recipes (>= 0.1.10), reshape2, stats, stats4,\nutils, withr (>= 2.0.0)"                                                                                                                                                                                                       
    ## cellranger           "rematch, tibble"                                                                                                                                                                                                                                                                                                                                                
    ## class                "MASS"                                                                                                                                                                                                                                                                                                                                                           
    ## cli                  "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## clipr                "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## clock                "cli (>= 3.6.4), lifecycle (>= 1.0.4), rlang (>= 1.1.5), tzdb\n(>= 0.5.0), vctrs (>= 0.6.5)"                                                                                                                                                                                                                                                                     
    ## cluster              "graphics, grDevices, stats, utils"                                                                                                                                                                                                                                                                                                                              
    ## codetools            NA                                                                                                                                                                                                                                                                                                                                                               
    ## colorspace           "graphics, grDevices, stats"                                                                                                                                                                                                                                                                                                                                     
    ## colourpicker         "ggplot2, htmltools, htmlwidgets (>= 0.7), jsonlite, miniUI (>=\n0.1.1), shiny (>= 0.11.1), shinyjs (>= 2.0.0), utils"                                                                                                                                                                                                                                           
    ## commonmark           NA                                                                                                                                                                                                                                                                                                                                                               
    ## compiler             NA                                                                                                                                                                                                                                                                                                                                                               
    ## corrplot             NA                                                                                                                                                                                                                                                                                                                                                               
    ## cowplot              "ggplot2 (>= 3.5.2), grid, gtable, grDevices, methods, rlang,\nscales"                                                                                                                                                                                                                                                                                           
    ## cpp11                NA                                                                                                                                                                                                                                                                                                                                                               
    ## crayon               "grDevices, methods, utils"                                                                                                                                                                                                                                                                                                                                      
    ## curl                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## data.table           "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## datasets             NA                                                                                                                                                                                                                                                                                                                                                               
    ## DelayedArray         "stats"                                                                                                                                                                                                                                                                                                                                                          
    ## Deriv                "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## DESeq2               "BiocGenerics (>= 0.7.5), Biobase, BiocParallel, matrixStats,\nmethods, stats4, locfit, ggplot2 (>= 3.4.0), Rcpp (>= 0.11.0),\nMatrixGenerics"                                                                                                                                                                                                                   
    ## diagram              "stats, graphics"                                                                                                                                                                                                                                                                                                                                                
    ## digest               "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## doBy                 "boot, broom, cowplot, Deriv, dplyr, ggplot2, MASS, Matrix,\nmodelr, microbenchmark, rlang, tibble, tidyr,"                                                                                                                                                                                                                                                      
    ## dplyr                "cli (>= 3.4.0), generics, glue (>= 1.3.2), lifecycle (>=\n1.0.3), magrittr (>= 1.5), methods, pillar (>= 1.9.0), R6,\nrlang (>= 1.1.0), tibble (>= 3.2.0), tidyselect (>= 1.2.0),\nutils, vctrs (>= 0.6.4)"                                                                                                                                                     
    ## dunn.test            NA                                                                                                                                                                                                                                                                                                                                                               
    ## e1071                "graphics, grDevices, class, stats, methods, utils, proxy"                                                                                                                                                                                                                                                                                                       
    ## emmeans              "estimability (>= 1.4.1), graphics, methods, mvtnorm, numDeriv,\nstats, utils"                                                                                                                                                                                                                                                                                   
    ## EnhancedVolcano      "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## estimability         NA                                                                                                                                                                                                                                                                                                                                                               
    ## evaluate             NA                                                                                                                                                                                                                                                                                                                                                               
    ## farver               NA                                                                                                                                                                                                                                                                                                                                                               
    ## fastmap              NA                                                                                                                                                                                                                                                                                                                                                               
    ## FlexParamCurve       "stats, utils"                                                                                                                                                                                                                                                                                                                                                   
    ## fontawesome          "rlang (>= 1.0.6), htmltools (>= 0.5.1.1)"                                                                                                                                                                                                                                                                                                                       
    ## forcats              "cli (>= 3.4.0), glue, lifecycle, magrittr, rlang (>= 1.0.0),\ntibble"                                                                                                                                                                                                                                                                                           
    ## foreach              "codetools, utils, iterators"                                                                                                                                                                                                                                                                                                                                    
    ## foreign              "methods, utils, stats"                                                                                                                                                                                                                                                                                                                                          
    ## formatR              NA                                                                                                                                                                                                                                                                                                                                                               
    ## Formula              NA                                                                                                                                                                                                                                                                                                                                                               
    ## fs                   "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## FSA                  "graphics, grDevices, stats, tools, utils, car, dunn.test,\nFlexParamCurve, lmtest, plotrix, purrr, withr"                                                                                                                                                                                                                                                       
    ## futile.logger        "utils, lambda.r (>= 1.1.0), futile.options"                                                                                                                                                                                                                                                                                                                     
    ## futile.options       NA                                                                                                                                                                                                                                                                                                                                                               
    ## future               "digest, globals (>= 0.18.0), listenv (>= 0.8.0), parallel,\nparallelly (>= 1.44.0), utils"                                                                                                                                                                                                                                                                      
    ## future.apply         "globals, parallel, utils"                                                                                                                                                                                                                                                                                                                                       
    ## generics             "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## GenomeInfoDb         "stats, stats4, utils, UCSC.utils, GenomeInfoDbData"                                                                                                                                                                                                                                                                                                             
    ## GenomeInfoDbData     NA                                                                                                                                                                                                                                                                                                                                                               
    ## GenomicRanges        "utils, stats, XVector (>= 0.29.2)"                                                                                                                                                                                                                                                                                                                              
    ## ggcorrplot           "reshape2, stats"                                                                                                                                                                                                                                                                                                                                                
    ## ggExtra              "colourpicker (>= 1.0), ggplot2 (>= 2.2.0), grDevices, grid (>=\n3.1.3), gtable (>= 0.2.0), miniUI (>= 0.1.1), scales (>=\n0.2.0), shiny (>= 0.13.0), shinyjs (>= 0.5.2), utils, R6"                                                                                                                                                                             
    ## ggplot2              "cli, glue, grDevices, grid, gtable (>= 0.1.1), isoband,\nlifecycle (> 1.0.1), MASS, mgcv, rlang (>= 1.1.0), scales (>=\n1.3.0), stats, tibble, vctrs (>= 0.6.0), withr (>= 2.5.0)"                                                                                                                                                                              
    ## ggpubr               "ggrepel (>= 0.9.2), grid, ggsci, stats, utils, tidyr (>=\n1.3.0), purrr, dplyr (>= 0.7.1), cowplot (>= 1.1.1), ggsignif,\nscales, gridExtra, glue, polynom, rlang (>= 0.4.6), rstatix (>=\n0.7.2), tibble, magrittr"                                                                                                                                            
    ## ggrepel              "grid, Rcpp, rlang (>= 0.3.0), scales (>= 0.5.0), withr (>=\n2.5.0)"                                                                                                                                                                                                                                                                                             
    ## ggsci                "ggplot2 (>= 2.0.0), grDevices, scales"                                                                                                                                                                                                                                                                                                                          
    ## ggsignif             "ggplot2 (>= 3.3.5)"                                                                                                                                                                                                                                                                                                                                             
    ## glmnet               "methods, utils, foreach, shape, survival, Rcpp"                                                                                                                                                                                                                                                                                                                 
    ## globals              "codetools"                                                                                                                                                                                                                                                                                                                                                      
    ## glue                 "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## gower                NA                                                                                                                                                                                                                                                                                                                                                               
    ## graphics             "grDevices"                                                                                                                                                                                                                                                                                                                                                      
    ## grDevices            NA                                                                                                                                                                                                                                                                                                                                                               
    ## grid                 "grDevices, utils"                                                                                                                                                                                                                                                                                                                                               
    ## gridExtra            "gtable, grid, grDevices, graphics, utils"                                                                                                                                                                                                                                                                                                                       
    ## gtable               "cli, glue, grid, lifecycle, rlang (>= 1.1.0), stats"                                                                                                                                                                                                                                                                                                            
    ## hardhat              "cli (>= 3.6.0), glue (>= 1.6.2), rlang (>= 1.1.0), sparsevctrs\n(>= 0.2.0), tibble (>= 3.2.1), vctrs (>= 0.6.0)"                                                                                                                                                                                                                                                
    ## haven                "cli (>= 3.0.0), forcats (>= 0.2.0), hms, lifecycle, methods,\nreadr (>= 0.1.0), rlang (>= 0.4.0), tibble, tidyselect, vctrs\n(>= 0.3.0)"                                                                                                                                                                                                                        
    ## highr                "xfun (>= 0.18)"                                                                                                                                                                                                                                                                                                                                                 
    ## hms                  "lifecycle, methods, pkgconfig, rlang (>= 1.0.2), vctrs (>=\n0.3.8)"                                                                                                                                                                                                                                                                                             
    ## htmltools            "base64enc, digest, fastmap (>= 1.1.0), grDevices, rlang (>=\n1.0.0), utils"                                                                                                                                                                                                                                                                                     
    ## htmlwidgets          "grDevices, htmltools (>= 0.5.7), jsonlite (>= 0.9.16), knitr\n(>= 1.8), rmarkdown, yaml"                                                                                                                                                                                                                                                                        
    ## httpuv               "later (>= 0.8.0), promises, R6, Rcpp (>= 1.0.7), utils"                                                                                                                                                                                                                                                                                                         
    ## httr                 "curl (>= 5.0.2), jsonlite, mime, openssl (>= 0.8), R6"                                                                                                                                                                                                                                                                                                          
    ## ipred                "rpart (>= 3.1-8), MASS, survival, nnet, class, prodlim"                                                                                                                                                                                                                                                                                                         
    ## IRanges              "stats4"                                                                                                                                                                                                                                                                                                                                                         
    ## isoband              "grid, utils"                                                                                                                                                                                                                                                                                                                                                    
    ## iterators            NA                                                                                                                                                                                                                                                                                                                                                               
    ## jquerylib            "htmltools"                                                                                                                                                                                                                                                                                                                                                      
    ## jsonlite             NA                                                                                                                                                                                                                                                                                                                                                               
    ## KernSmooth           NA                                                                                                                                                                                                                                                                                                                                                               
    ## knitr                "evaluate (>= 0.15), highr (>= 0.11), methods, tools, xfun (>=\n0.51), yaml (>= 2.1.19)"                                                                                                                                                                                                                                                                         
    ## labeling             "stats, graphics"                                                                                                                                                                                                                                                                                                                                                
    ## lambda.r             "formatR"                                                                                                                                                                                                                                                                                                                                                        
    ## later                "Rcpp (>= 0.12.9), rlang"                                                                                                                                                                                                                                                                                                                                        
    ## lattice              "grid, grDevices, graphics, stats, utils"                                                                                                                                                                                                                                                                                                                        
    ## lava                 "cli, future.apply, graphics, grDevices, methods, numDeriv,\nprogressr, stats, survival, SQUAREM, utils"                                                                                                                                                                                                                                                         
    ## lifecycle            "cli (>= 3.4.0), glue, rlang (>= 1.1.0)"                                                                                                                                                                                                                                                                                                                         
    ## listenv              NA                                                                                                                                                                                                                                                                                                                                                               
    ## lme4                 "graphics, grid, splines, utils, parallel, MASS, lattice, boot,\nnlme (>= 3.1-123), minqa (>= 1.1.15), nloptr (>= 1.0.4),\nreformulas (>= 0.3.0)"                                                                                                                                                                                                                
    ## lmtest               "graphics"                                                                                                                                                                                                                                                                                                                                                       
    ## locfit               "lattice"                                                                                                                                                                                                                                                                                                                                                        
    ## lubridate            "generics, timechange (>= 0.3.0)"                                                                                                                                                                                                                                                                                                                                
    ## magrittr             NA                                                                                                                                                                                                                                                                                                                                                               
    ## MASS                 "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## Matrix               "grDevices, graphics, grid, lattice, stats, utils"                                                                                                                                                                                                                                                                                                               
    ## MatrixGenerics       "methods"                                                                                                                                                                                                                                                                                                                                                        
    ## MatrixModels         "stats, methods, Matrix (>= 1.6-0), Matrix(< 1.8-0)"                                                                                                                                                                                                                                                                                                             
    ## matrixStats          NA                                                                                                                                                                                                                                                                                                                                                               
    ## memoise              "rlang (>= 0.4.10), cachem"                                                                                                                                                                                                                                                                                                                                      
    ## methods              "utils, stats"                                                                                                                                                                                                                                                                                                                                                   
    ## mgcv                 "methods, stats, graphics, Matrix, splines, utils"                                                                                                                                                                                                                                                                                                               
    ## microbenchmark       "graphics, stats"                                                                                                                                                                                                                                                                                                                                                
    ## mime                 "tools"                                                                                                                                                                                                                                                                                                                                                          
    ## miniUI               "shiny (>= 0.13), htmltools (>= 0.3), utils"                                                                                                                                                                                                                                                                                                                     
    ## minqa                "Rcpp (>= 0.9.10)"                                                                                                                                                                                                                                                                                                                                               
    ## ModelMetrics         "Rcpp, data.table"                                                                                                                                                                                                                                                                                                                                               
    ## modelr               "broom, magrittr, purrr (>= 0.2.2), rlang (>= 1.0.6), tibble,\ntidyr (>= 0.8.0), tidyselect, vctrs"                                                                                                                                                                                                                                                              
    ## moments              NA                                                                                                                                                                                                                                                                                                                                                               
    ## mvtnorm              "stats"                                                                                                                                                                                                                                                                                                                                                          
    ## nlme                 "graphics, stats, utils, lattice"                                                                                                                                                                                                                                                                                                                                
    ## nloptr               NA                                                                                                                                                                                                                                                                                                                                                               
    ## nnet                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## numDeriv             NA                                                                                                                                                                                                                                                                                                                                                               
    ## openssl              "askpass"                                                                                                                                                                                                                                                                                                                                                        
    ## parallel             "tools, compiler"                                                                                                                                                                                                                                                                                                                                                
    ## parallelly           "parallel, tools, utils"                                                                                                                                                                                                                                                                                                                                         
    ## patchwork            "ggplot2 (>= 3.0.0), gtable (>= 0.3.6), grid, stats, grDevices,\nutils, graphics, rlang (>= 1.0.0), cli, farver"                                                                                                                                                                                                                                                 
    ## pbkrtest             "broom, dplyr, MASS, methods, numDeriv, Matrix (>= 1.2.3), doBy\n(>= 4.6.22)"                                                                                                                                                                                                                                                                                    
    ## pillar               "cli (>= 2.3.0), glue, lifecycle, rlang (>= 1.0.2), utf8 (>=\n1.1.0), utils, vctrs (>= 0.5.0)"                                                                                                                                                                                                                                                                   
    ## pkgconfig            "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## plotrix              "grDevices, graphics, stats, utils"                                                                                                                                                                                                                                                                                                                              
    ## plyr                 "Rcpp (>= 0.11.0)"                                                                                                                                                                                                                                                                                                                                               
    ## polynom              "stats, graphics"                                                                                                                                                                                                                                                                                                                                                
    ## ppcor                NA                                                                                                                                                                                                                                                                                                                                                               
    ## prettyunits          NA                                                                                                                                                                                                                                                                                                                                                               
    ## pROC                 "methods, plyr, Rcpp (>= 0.11.1)"                                                                                                                                                                                                                                                                                                                                
    ## processx             "ps (>= 1.2.0), R6, utils"                                                                                                                                                                                                                                                                                                                                       
    ## prodlim              "Rcpp (>= 0.11.5), stats, rlang, data.table, grDevices,\nggplot2, graphics, diagram, survival, KernSmooth, lava"                                                                                                                                                                                                                                                 
    ## progress             "crayon, hms, prettyunits, R6"                                                                                                                                                                                                                                                                                                                                   
    ## progressr            "digest, utils"                                                                                                                                                                                                                                                                                                                                                  
    ## promises             "fastmap (>= 1.1.0), later, magrittr (>= 1.5), R6, Rcpp, rlang,\nstats"                                                                                                                                                                                                                                                                                          
    ## proxy                "stats, utils"                                                                                                                                                                                                                                                                                                                                                   
    ## ps                   "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## purrr                "cli (>= 3.6.1), lifecycle (>= 1.0.3), magrittr (>= 1.5.0),\nrlang (>= 1.1.1), vctrs (>= 0.6.3)"                                                                                                                                                                                                                                                                 
    ## quantreg             "methods, graphics, Matrix, MatrixModels, survival, MASS"                                                                                                                                                                                                                                                                                                        
    ## quarto               "cli, fs, htmltools, jsonlite, later, lifecycle, processx,\nrlang, rmarkdown, rstudioapi, tools, utils, xfun, yaml (>=\n2.3.10)"                                                                                                                                                                                                                                 
    ## R.methodsS3          "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## R.oo                 "methods, utils"                                                                                                                                                                                                                                                                                                                                                 
    ## R.utils              "methods, utils, tools, R.methodsS3"                                                                                                                                                                                                                                                                                                                             
    ## R6                   NA                                                                                                                                                                                                                                                                                                                                                               
    ## rappdirs             NA                                                                                                                                                                                                                                                                                                                                                               
    ## rbibutils            "utils, tools"                                                                                                                                                                                                                                                                                                                                                   
    ## RColorBrewer         NA                                                                                                                                                                                                                                                                                                                                                               
    ## Rcpp                 "methods, utils"                                                                                                                                                                                                                                                                                                                                                 
    ## RcppArmadillo        "Rcpp (>= 1.0.12), stats, utils, methods"                                                                                                                                                                                                                                                                                                                        
    ## RcppEigen            "Rcpp (>= 0.11.0), stats, utils"                                                                                                                                                                                                                                                                                                                                 
    ## Rdpack               "tools, utils, rbibutils (>= 1.3)"                                                                                                                                                                                                                                                                                                                               
    ## readr                "cli (>= 3.2.0), clipr, crayon, hms (>= 0.4.1), lifecycle (>=\n0.2.0), methods, R6, rlang, tibble, utils, vroom (>= 1.6.0)"                                                                                                                                                                                                                                      
    ## readxl               "cellranger, tibble (>= 2.0.1), utils"                                                                                                                                                                                                                                                                                                                           
    ## recipes              "cli, clock (>= 0.6.1), generics (>= 0.1.2), glue, gower,\nhardhat (>= 1.4.1), ipred (>= 0.9-12), lifecycle (>= 1.0.3),\nlubridate (>= 1.8.0), magrittr, Matrix, purrr (>= 1.0.0), rlang\n(>= 1.1.0), sparsevctrs (>= 0.3.3), stats, tibble, tidyr (>=\n1.0.0), tidyselect (>= 1.2.0), timeDate, utils, vctrs (>=\n0.5.0), withr"                                
    ## reformulas           "stats, methods, Matrix, Rdpack"                                                                                                                                                                                                                                                                                                                                 
    ## rematch              NA                                                                                                                                                                                                                                                                                                                                                               
    ## reshape2             "plyr (>= 1.8.1), Rcpp, stringr"                                                                                                                                                                                                                                                                                                                                 
    ## rio                  "tools, stats, utils, foreign, haven (>= 1.1.2), curl (>= 0.6),\ndata.table (>= 1.11.2), readxl (>= 0.1.1), tibble, writexl,\nlifecycle, R.utils, readr"                                                                                                                                                                                                         
    ## rlang                "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## rmarkdown            "bslib (>= 0.2.5.1), evaluate (>= 0.13), fontawesome (>=\n0.5.0), htmltools (>= 0.5.1), jquerylib, jsonlite, knitr (>=\n1.43), methods, tinytex (>= 0.31), tools, utils, xfun (>=\n0.36), yaml (>= 2.1.19)"                                                                                                                                                      
    ## rpart                NA                                                                                                                                                                                                                                                                                                                                                               
    ## rstatix              "stats, utils, tidyr (>= 1.0.0), purrr, broom (>= 0.7.4), rlang\n(>= 0.3.1), tibble (>= 2.1.3), dplyr (>= 0.7.1), magrittr,\ncorrplot, tidyselect (>= 1.2.0), car, generics (>= 0.0.2)"                                                                                                                                                                          
    ## rstudioapi           NA                                                                                                                                                                                                                                                                                                                                                               
    ## S4Arrays             "stats, crayon"                                                                                                                                                                                                                                                                                                                                                  
    ## S4Vectors            NA                                                                                                                                                                                                                                                                                                                                                               
    ## sass                 "fs (>= 1.2.4), rlang (>= 0.4.10), htmltools (>= 0.5.1), R6,\nrappdirs"                                                                                                                                                                                                                                                                                          
    ## scales               "cli, farver (>= 2.0.3), glue, labeling, lifecycle, R6,\nRColorBrewer, rlang (>= 1.1.0), viridisLite"                                                                                                                                                                                                                                                            
    ## shape                "stats, graphics, grDevices"                                                                                                                                                                                                                                                                                                                                     
    ## shiny                "utils, grDevices, httpuv (>= 1.5.2), mime (>= 0.3), jsonlite\n(>= 0.9.16), xtable, fontawesome (>= 0.4.0), htmltools (>=\n0.5.4), R6 (>= 2.0), sourcetools, later (>= 1.0.0), promises\n(>= 1.3.2), tools, cli, rlang (>= 0.4.10), fastmap (>= 1.1.1),\nwithr, commonmark (>= 1.7), glue (>= 1.3.2), bslib (>= 0.6.0),\ncachem (>= 1.1.0), lifecycle (>= 0.2.0)"
    ## shinyjs              "digest (>= 0.6.8), jsonlite, shiny (>= 1.0.0)"                                                                                                                                                                                                                                                                                                                  
    ## snow                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## sourcetools          NA                                                                                                                                                                                                                                                                                                                                                               
    ## SparseArray          "utils, stats, matrixStats, IRanges, XVector"                                                                                                                                                                                                                                                                                                                    
    ## SparseM              "graphics, stats, utils"                                                                                                                                                                                                                                                                                                                                         
    ## sparsevctrs          "cli (>= 3.4.0), rlang (>= 1.1.0), vctrs"                                                                                                                                                                                                                                                                                                                        
    ## spatial              NA                                                                                                                                                                                                                                                                                                                                                               
    ## splines              "graphics, stats"                                                                                                                                                                                                                                                                                                                                                
    ## SQUAREM              NA                                                                                                                                                                                                                                                                                                                                                               
    ## stats                "utils, grDevices, graphics"                                                                                                                                                                                                                                                                                                                                     
    ## stats4               "graphics, methods, stats"                                                                                                                                                                                                                                                                                                                                       
    ## stringi              "tools, utils, stats"                                                                                                                                                                                                                                                                                                                                            
    ## stringr              "cli, glue (>= 1.6.1), lifecycle (>= 1.0.3), magrittr, rlang\n(>= 1.0.0), stringi (>= 1.5.3), vctrs (>= 0.4.0)"                                                                                                                                                                                                                                                  
    ## SummarizedExperiment "utils, stats, tools, Matrix, BiocGenerics (>= 0.51.3),\nS4Vectors (>= 0.33.7), IRanges (>= 2.23.9), GenomeInfoDb (>=\n1.13.1), S4Arrays (>= 1.1.1), DelayedArray (>= 0.31.12)"                                                                                                                                                                                  
    ## survival             "graphics, Matrix, methods, splines, stats, utils"                                                                                                                                                                                                                                                                                                               
    ## sys                  NA                                                                                                                                                                                                                                                                                                                                                               
    ## tcltk                "utils"                                                                                                                                                                                                                                                                                                                                                          
    ## tibble               "cli, lifecycle (>= 1.0.0), magrittr, methods, pillar (>=\n1.8.1), pkgconfig, rlang (>= 1.0.2), utils, vctrs (>= 0.5.0)"                                                                                                                                                                                                                                         
    ## tidyr                "cli (>= 3.4.1), dplyr (>= 1.0.10), glue, lifecycle (>= 1.0.3),\nmagrittr, purrr (>= 1.0.1), rlang (>= 1.1.1), stringr (>=\n1.5.0), tibble (>= 2.1.1), tidyselect (>= 1.2.0), utils, vctrs\n(>= 0.5.2)"                                                                                                                                                          
    ## tidyselect           "cli (>= 3.3.0), glue (>= 1.3.0), lifecycle (>= 1.0.3), rlang\n(>= 1.0.4), vctrs (>= 0.5.2), withr"                                                                                                                                                                                                                                                              
    ## timechange           NA                                                                                                                                                                                                                                                                                                                                                               
    ## timeDate             "graphics, utils, stats"                                                                                                                                                                                                                                                                                                                                         
    ## tinytex              "xfun (>= 0.48)"                                                                                                                                                                                                                                                                                                                                                 
    ## titanic              NA                                                                                                                                                                                                                                                                                                                                                               
    ## tools                NA                                                                                                                                                                                                                                                                                                                                                               
    ## translations         NA                                                                                                                                                                                                                                                                                                                                                               
    ## tzdb                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## UCSC.utils           "methods, stats, httr, jsonlite, S4Vectors"                                                                                                                                                                                                                                                                                                                      
    ## utf8                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## utils                NA                                                                                                                                                                                                                                                                                                                                                               
    ## vcd                  "stats, utils, MASS, grDevices, colorspace, lmtest"                                                                                                                                                                                                                                                                                                              
    ## vctrs                "cli (>= 3.4.0), glue, lifecycle (>= 1.0.3), rlang (>= 1.1.0)"                                                                                                                                                                                                                                                                                                   
    ## viridisLite          NA                                                                                                                                                                                                                                                                                                                                                               
    ## vroom                "bit64, cli (>= 3.2.0), crayon, glue, hms, lifecycle (>=\n1.0.3), methods, rlang (>= 0.4.2), stats, tibble (>= 2.0.0),\ntidyselect, tzdb (>= 0.1.1), vctrs (>= 0.2.0), withr"                                                                                                                                                                                    
    ## withr                "graphics, grDevices"                                                                                                                                                                                                                                                                                                                                            
    ## writexl              NA                                                                                                                                                                                                                                                                                                                                                               
    ## xfun                 "grDevices, stats, tools"                                                                                                                                                                                                                                                                                                                                        
    ## xtable               "stats, utils"                                                                                                                                                                                                                                                                                                                                                   
    ## XVector              "methods, utils, tools, BiocGenerics, S4Vectors, IRanges"                                                                                                                                                                                                                                                                                                        
    ## yaml                 NA                                                                                                                                                                                                                                                                                                                                                               
    ## zoo                  "utils, graphics, grDevices, lattice (>= 0.20-27)"                                                                                                                                                                                                                                                                                                               
    ##                      LinkingTo                                                       
    ## abind                NA                                                              
    ## askpass              NA                                                              
    ## backports            NA                                                              
    ## base                 NA                                                              
    ## base64enc            NA                                                              
    ## BH                   NA                                                              
    ## Biobase              NA                                                              
    ## BiocGenerics         NA                                                              
    ## BiocManager          NA                                                              
    ## BiocParallel         "BH (>= 1.87.0), cpp11"                                         
    ## BiocVersion          NA                                                              
    ## bit                  NA                                                              
    ## bit64                NA                                                              
    ## boot                 NA                                                              
    ## broom                NA                                                              
    ## bslib                NA                                                              
    ## cachem               NA                                                              
    ## car                  NA                                                              
    ## carData              NA                                                              
    ## caret                NA                                                              
    ## cellranger           NA                                                              
    ## class                NA                                                              
    ## cli                  NA                                                              
    ## clipr                NA                                                              
    ## clock                "cpp11 (>= 0.5.2), tzdb (>= 0.5.0)"                             
    ## cluster              NA                                                              
    ## codetools            NA                                                              
    ## colorspace           NA                                                              
    ## colourpicker         NA                                                              
    ## commonmark           NA                                                              
    ## compiler             NA                                                              
    ## corrplot             NA                                                              
    ## cowplot              NA                                                              
    ## cpp11                NA                                                              
    ## crayon               NA                                                              
    ## curl                 NA                                                              
    ## data.table           NA                                                              
    ## datasets             NA                                                              
    ## DelayedArray         "S4Vectors"                                                     
    ## Deriv                NA                                                              
    ## DESeq2               "Rcpp, RcppArmadillo"                                           
    ## diagram              NA                                                              
    ## digest               NA                                                              
    ## doBy                 NA                                                              
    ## dplyr                NA                                                              
    ## dunn.test            NA                                                              
    ## e1071                NA                                                              
    ## emmeans              NA                                                              
    ## EnhancedVolcano      NA                                                              
    ## estimability         NA                                                              
    ## evaluate             NA                                                              
    ## farver               NA                                                              
    ## fastmap              NA                                                              
    ## FlexParamCurve       NA                                                              
    ## fontawesome          NA                                                              
    ## forcats              NA                                                              
    ## foreach              NA                                                              
    ## foreign              NA                                                              
    ## formatR              NA                                                              
    ## Formula              NA                                                              
    ## fs                   NA                                                              
    ## FSA                  NA                                                              
    ## futile.logger        NA                                                              
    ## futile.options       NA                                                              
    ## future               NA                                                              
    ## future.apply         NA                                                              
    ## generics             NA                                                              
    ## GenomeInfoDb         NA                                                              
    ## GenomeInfoDbData     NA                                                              
    ## GenomicRanges        "S4Vectors, IRanges"                                            
    ## ggcorrplot           NA                                                              
    ## ggExtra              NA                                                              
    ## ggplot2              NA                                                              
    ## ggpubr               NA                                                              
    ## ggrepel              "Rcpp"                                                          
    ## ggsci                NA                                                              
    ## ggsignif             NA                                                              
    ## glmnet               "RcppEigen, Rcpp"                                               
    ## globals              NA                                                              
    ## glue                 NA                                                              
    ## gower                NA                                                              
    ## graphics             NA                                                              
    ## grDevices            NA                                                              
    ## grid                 NA                                                              
    ## gridExtra            NA                                                              
    ## gtable               NA                                                              
    ## hardhat              NA                                                              
    ## haven                "cpp11"                                                         
    ## highr                NA                                                              
    ## hms                  NA                                                              
    ## htmltools            NA                                                              
    ## htmlwidgets          NA                                                              
    ## httpuv               "later, Rcpp"                                                   
    ## httr                 NA                                                              
    ## ipred                NA                                                              
    ## IRanges              "S4Vectors"                                                     
    ## isoband              NA                                                              
    ## iterators            NA                                                              
    ## jquerylib            NA                                                              
    ## jsonlite             NA                                                              
    ## KernSmooth           NA                                                              
    ## knitr                NA                                                              
    ## labeling             NA                                                              
    ## lambda.r             NA                                                              
    ## later                "Rcpp"                                                          
    ## lattice              NA                                                              
    ## lava                 NA                                                              
    ## lifecycle            NA                                                              
    ## listenv              NA                                                              
    ## lme4                 "Rcpp (>= 0.10.5), RcppEigen (>= 0.3.3.9.4), Matrix (>=\n1.2-3)"
    ## lmtest               NA                                                              
    ## locfit               NA                                                              
    ## lubridate            NA                                                              
    ## magrittr             NA                                                              
    ## MASS                 NA                                                              
    ## Matrix               NA                                                              
    ## MatrixGenerics       NA                                                              
    ## MatrixModels         NA                                                              
    ## matrixStats          NA                                                              
    ## memoise              NA                                                              
    ## methods              NA                                                              
    ## mgcv                 NA                                                              
    ## microbenchmark       NA                                                              
    ## mime                 NA                                                              
    ## miniUI               NA                                                              
    ## minqa                "Rcpp"                                                          
    ## ModelMetrics         "Rcpp"                                                          
    ## modelr               NA                                                              
    ## moments              NA                                                              
    ## mvtnorm              NA                                                              
    ## nlme                 NA                                                              
    ## nloptr               NA                                                              
    ## nnet                 NA                                                              
    ## numDeriv             NA                                                              
    ## openssl              NA                                                              
    ## parallel             NA                                                              
    ## parallelly           NA                                                              
    ## patchwork            NA                                                              
    ## pbkrtest             NA                                                              
    ## pillar               NA                                                              
    ## pkgconfig            NA                                                              
    ## plotrix              NA                                                              
    ## plyr                 "Rcpp"                                                          
    ## polynom              NA                                                              
    ## ppcor                NA                                                              
    ## prettyunits          NA                                                              
    ## pROC                 "Rcpp"                                                          
    ## processx             NA                                                              
    ## prodlim              "Rcpp"                                                          
    ## progress             NA                                                              
    ## progressr            NA                                                              
    ## promises             "later, Rcpp"                                                   
    ## proxy                NA                                                              
    ## ps                   NA                                                              
    ## purrr                "cli"                                                           
    ## quantreg             NA                                                              
    ## quarto               NA                                                              
    ## R.methodsS3          NA                                                              
    ## R.oo                 NA                                                              
    ## R.utils              NA                                                              
    ## R6                   NA                                                              
    ## rappdirs             NA                                                              
    ## rbibutils            NA                                                              
    ## RColorBrewer         NA                                                              
    ## Rcpp                 NA                                                              
    ## RcppArmadillo        "Rcpp"                                                          
    ## RcppEigen            "Rcpp"                                                          
    ## Rdpack               NA                                                              
    ## readr                "cpp11, tzdb (>= 0.1.1)"                                        
    ## readxl               "cpp11 (>= 0.4.0), progress"                                    
    ## recipes              NA                                                              
    ## reformulas           NA                                                              
    ## rematch              NA                                                              
    ## reshape2             "Rcpp"                                                          
    ## rio                  NA                                                              
    ## rlang                NA                                                              
    ## rmarkdown            NA                                                              
    ## rpart                NA                                                              
    ## rstatix              NA                                                              
    ## rstudioapi           NA                                                              
    ## S4Arrays             "S4Vectors"                                                     
    ## S4Vectors            NA                                                              
    ## sass                 NA                                                              
    ## scales               NA                                                              
    ## shape                NA                                                              
    ## shiny                NA                                                              
    ## shinyjs              NA                                                              
    ## snow                 NA                                                              
    ## sourcetools          NA                                                              
    ## SparseArray          "S4Vectors, IRanges, XVector"                                   
    ## SparseM              NA                                                              
    ## sparsevctrs          NA                                                              
    ## spatial              NA                                                              
    ## splines              NA                                                              
    ## SQUAREM              NA                                                              
    ## stats                NA                                                              
    ## stats4               NA                                                              
    ## stringi              NA                                                              
    ## stringr              NA                                                              
    ## SummarizedExperiment NA                                                              
    ## survival             NA                                                              
    ## sys                  NA                                                              
    ## tcltk                NA                                                              
    ## tibble               NA                                                              
    ## tidyr                "cpp11 (>= 0.4.0)"                                              
    ## tidyselect           NA                                                              
    ## timechange           "cpp11 (>= 0.2.7)"                                              
    ## timeDate             NA                                                              
    ## tinytex              NA                                                              
    ## titanic              NA                                                              
    ## tools                NA                                                              
    ## translations         NA                                                              
    ## tzdb                 "cpp11 (>= 0.5.2)"                                              
    ## UCSC.utils           NA                                                              
    ## utf8                 NA                                                              
    ## utils                NA                                                              
    ## vcd                  NA                                                              
    ## vctrs                NA                                                              
    ## viridisLite          NA                                                              
    ## vroom                "cpp11 (>= 0.2.0), progress (>= 1.2.1), tzdb (>= 0.1.1)"        
    ## withr                NA                                                              
    ## writexl              NA                                                              
    ## xfun                 NA                                                              
    ## xtable               NA                                                              
    ## XVector              "S4Vectors, IRanges"                                            
    ## yaml                 NA                                                              
    ## zoo                  NA                                                              
    ##                      Suggests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## abind                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## askpass              "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## backports            NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## base                 "methods"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## base64enc            NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## BH                   NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## Biobase              "tools, tkWidgets, ALL, RUnit, golubEsets, BiocStyle, knitr,\nlimma"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## BiocGenerics         "Biobase, S4Vectors, IRanges, S4Arrays, SparseArray,\nDelayedArray, HDF5Array, GenomicRanges, pwalign, Rsamtools,\nAnnotationDbi, affy, affyPLM, DESeq2, flowClust, MSnbase,\nannotate, MultiAssayExperiment, RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## BiocManager          "BiocVersion, BiocStyle, remotes, rmarkdown, testthat, withr,\ncurl, knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## BiocParallel         "BiocGenerics, tools, foreach, BBmisc, doParallel,\nGenomicRanges, RNAseqData.HNRNPC.bam.chr14,\nTxDb.Hsapiens.UCSC.hg19.knownGene, VariantAnnotation,\nRsamtools, GenomicAlignments, ShortRead, RUnit, BiocStyle,\nknitr, batchtools, data.table"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## BiocVersion          NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## bit                  "testthat (>= 3.0.0), roxygen2, knitr, markdown, rmarkdown,\nmicrobenchmark, bit64 (>= 4.0.0), ff (>= 4.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## bit64                "testthat (>= 3.0.3), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## boot                 "MASS, survival"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## broom                "AER, AUC, bbmle, betareg (>= 3.2-1), biglm, binGroup, boot,\nbtergm (>= 1.10.6), car (>= 3.1-2), carData, caret, cluster,\ncmprsk, coda, covr, drc, e1071, emmeans, epiR, ergm (>=\n3.10.4), fixest (>= 0.9.0), gam (>= 1.15), gee, geepack,\nggplot2, glmnet, glmnetUtils, gmm, Hmisc, irlba, interp,\njoineRML, Kendall, knitr, ks, Lahman, lavaan (>= 0.6.18),\nleaps, lfe, lm.beta, lme4, lmodel2, lmtest (>= 0.9.38),\nlsmeans, maps, margins, MASS, mclust, mediation, metafor, mfx,\nmgcv, mlogit, modeldata, modeltests (>= 0.1.6), muhaz,\nmultcomp, network, nnet, ordinal, plm, poLCA, psych, quantreg,\nrmarkdown, robust, robustbase, rsample, sandwich, spdep (>=\n1.1), spatialreg, speedglm, spelling, survey, survival (>=\n3.6-4), systemfit, testthat (>= 3.0.0), tseries, vars, zoo"
    ## bslib                "bsicons, curl, fontawesome, future, ggplot2, knitr, magrittr,\nrappdirs, rmarkdown (>= 2.7), shiny (> 1.8.1), testthat,\nthematic, tools, utils, withr, yaml"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## cachem               "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## car                  "alr4, boot, coxme, effects, knitr, leaps, lmtest, Matrix,\nMatrixModels, ordinal, plotrix, mvtnorm, rgl (>= 0.111.3), rio,\nsandwich, SparseM, survival, survey"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    ## carData              "car (>= 3.0-0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## caret                "BradleyTerry2, covr, Cubist, dplyr, earth (>= 2.2-3),\nellipse, fastICA, gam (>= 1.15), ipred, kernlab, klaR, knitr,\nMASS, Matrix, mda, mgcv, mlbench, MLmetrics, nnet, pamr, party\n(>= 0.9-99992), pls, proxy, randomForest, RANN, rmarkdown,\nrpart, spls, superpc, testthat (>= 0.9.1), themis (>= 0.1.3)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## cellranger           "covr, testthat (>= 1.0.0), knitr, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## class                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## cli                  "callr, covr, crayon, digest, glue (>= 1.6.0), grDevices,\nhtmltools, htmlwidgets, knitr, methods, processx, ps (>=\n1.3.4.9000), rlang (>= 1.0.2.9003), rmarkdown, rprojroot,\nrstudioapi, testthat (>= 3.2.0), tibble, whoami, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## clipr                "covr, knitr, rmarkdown, rstudioapi (>= 0.5), testthat (>=\n2.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## clock                "covr, knitr, magrittr, pillar, rmarkdown, slider (>= 0.3.2),\ntestthat (>= 3.0.0), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## cluster              "MASS, Matrix"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## codetools            NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## colorspace           "datasets, utils, KernSmooth, MASS, kernlab, mvtnorm, vcd,\ntcltk, shiny, shinyjs, ggplot2, dplyr, scales, grid, png, jpeg,\nknitr, rmarkdown, RColorBrewer, rcartocolor, scico, viridis,\nwesanderson"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## colourpicker         "knitr (>= 1.7), rmarkdown, rstudioapi (>= 0.5),\nshinydisconnect"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## commonmark           "curl, testthat, xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## compiler             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## corrplot             "seriation, knitr, RColorBrewer, rmarkdown, magrittr,\nprettydoc, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## cowplot              "Cairo, covr, dplyr, forcats, gridGraphics (>= 0.4-0), knitr,\nlattice, magick, maps, PASWR, patchwork, rmarkdown, ragg,\ntestthat (>= 1.0.0), tidyr, vdiffr (>= 0.3.0), VennDiagram"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## cpp11                "bench, brio, callr, cli, covr, decor, desc, ggplot2, glue,\nknitr, lobstr, mockery, progress, rmarkdown, scales, Rcpp,\ntestthat (>= 3.2.0), tibble, utils, vctrs, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## crayon               "mockery, rstudioapi, testthat, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## curl                 "spelling, testthat (>= 1.0.0), knitr, jsonlite, later,\nrmarkdown, httpuv (>= 1.4.4), webutils"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## data.table           "bit64 (>= 4.0.0), bit (>= 4.0.4), R.utils, xts, zoo (>=\n1.8-1), yaml, knitr, markdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## datasets             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## DelayedArray         "BiocParallel, HDF5Array (>= 1.17.12), genefilter,\nSummarizedExperiment, airway, lobstr, DelayedMatrixStats,\nknitr, rmarkdown, BiocStyle, RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## Deriv                "testthat (>= 0.11.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## DESeq2               "testthat, knitr, rmarkdown, vsn, pheatmap, RColorBrewer,\napeglm, ashr, tximport, tximeta, tximportData, readr, pbapply,\nairway, glmGamPoi, BiocManager"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## diagram              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## digest               "tinytest, simplermarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## doBy                 "geepack, knitr, lme4, markdown, multcomp, pbkrtest (>=\n0.5.2), survival, testthat (>= 2.1.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## dplyr                "bench, broom, callr, covr, DBI, dbplyr (>= 2.2.1), ggplot2,\nknitr, Lahman, lobstr, microbenchmark, nycflights13, purrr,\nrmarkdown, RMySQL, RPostgreSQL, RSQLite, stringi (>= 1.7.6),\ntestthat (>= 3.1.5), tidyr (>= 1.3.0), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## dunn.test            NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## e1071                "cluster, mlbench, nnet, randomForest, rpart, SparseM, xtable,\nMatrix, MASS, slam"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## emmeans              "bayesplot, bayestestR, biglm, brms, car, coda (>= 0.17),\ncompositions, ggplot2, knitr, lattice, lme4, lmerTest (>=\n2.0.32), logspline, MASS, mediation, mgcv, multcomp,\nmultcompView, MuMIn, nlme, ordinal (>= 2014.11-12), pbkrtest\n(>= 0.4-1), rmarkdown, rsm, sandwich, scales, splines,\ntestthat, tibble, xtable (>= 1.8-2)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## EnhancedVolcano      "ggalt, ggrastr, RUnit, BiocGenerics, knitr, DESeq2, pasilla,\nairway, org.Hs.eg.db, gridExtra, magrittr, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## estimability         "knitr, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## evaluate             "callr, covr, ggplot2 (>= 3.3.6), lattice, methods, pkgload,\nragg (>= 1.4.0), rlang (>= 1.1.5), knitr, testthat (>= 3.0.0),\nwithr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## farver               "covr, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## fastmap              "testthat (>= 2.1.1)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## FlexParamCurve       NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## fontawesome          "covr, dplyr (>= 1.0.8), gt (>= 0.9.0), knitr (>= 1.31),\ntestthat (>= 3.0.0), rsvg"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## forcats              "covr, dplyr, ggplot2, knitr, readr, rmarkdown, testthat (>=\n3.0.0), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## foreach              "randomForest, doMC, doParallel, testthat, knitr, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## foreign              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## formatR              "rstudioapi, shiny, testit, rmarkdown, knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## Formula              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## fs                   "covr, crayon, knitr, pillar (>= 1.0.0), rmarkdown, spelling,\ntestthat (>= 3.0.0), tibble (>= 1.1.0), vctrs (>= 0.3.0), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## FSA                  "dplyr, fishmethods, FSAdata, knitr, nlme, nlstools,\nrmarkdown, testthat (>= 3.0.0), tidyr, covr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## futile.logger        "testthat, jsonlite"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## futile.options       NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## future               "methods, RhpcBLASctl, R.rsp, markdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## future.apply         "datasets, stats, tools, listenv, R.rsp, markdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## generics             "covr, pkgload, testthat (>= 3.0.0), tibble, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## GenomeInfoDb         "R.utils, data.table, GenomicRanges, Rsamtools,\nGenomicAlignments, GenomicFeatures, BSgenome,\nTxDb.Dmelanogaster.UCSC.dm3.ensGene,\nBSgenome.Scerevisiae.UCSC.sacCer2, BSgenome.Celegans.UCSC.ce2,\nBSgenome.Hsapiens.NCBI.GRCh38, RUnit, BiocStyle, knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## GenomeInfoDbData     NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## GenomicRanges        "Matrix, Biobase, AnnotationDbi, annotate, Biostrings (>=\n2.25.3), SummarizedExperiment (>= 0.1.5), Rsamtools (>=\n1.13.53), GenomicAlignments, rtracklayer, BSgenome,\nGenomicFeatures, txdbmaker, Gviz, VariantAnnotation,\nAnnotationHub, DESeq2, DEXSeq, edgeR, KEGGgraph,\nRNAseqData.HNRNPC.bam.chr14, pasillaBamSubset, KEGGREST,\nhgu95av2.db, hgu95av2probe, BSgenome.Scerevisiae.UCSC.sacCer2,\nBSgenome.Hsapiens.UCSC.hg38, BSgenome.Mmusculus.UCSC.mm10,\nTxDb.Athaliana.BioMart.plantsmart22,\nTxDb.Dmelanogaster.UCSC.dm3.ensGene,\nTxDb.Hsapiens.UCSC.hg38.knownGene,\nTxDb.Mmusculus.UCSC.mm10.knownGene, RUnit, digest, knitr,\nrmarkdown, BiocStyle"                                                                                                                                  
    ## ggcorrplot           "testthat (>= 3.0.0), knitr, spelling, vdiffr (>= 1.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## ggExtra              "knitr (>= 1.7), rmarkdown, rstudioapi (>= 0.5), testthat,\nvdiffr, fontquiver, svglite, withr, devtools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## ggplot2              "covr, dplyr, ggplot2movies, hexbin, Hmisc, knitr, mapproj,\nmaps, multcomp, munsell, nlme, profvis, quantreg, ragg (>=\n1.2.6), RColorBrewer, rmarkdown, rpart, sf (>= 0.7-3), svglite\n(>= 2.1.2), testthat (>= 3.1.2), vdiffr (>= 1.0.6), xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## ggpubr               "grDevices, knitr, RColorBrewer, gtable, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## ggrepel              "knitr, rmarkdown, testthat, svglite, vdiffr, gridExtra, ggpp,\npatchwork, devtools, prettydoc, ggbeeswarm, dplyr, magrittr,\nreadr, stringr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## ggsci                "gridExtra, knitr, ragg, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## ggsignif             "knitr, rmarkdown, testthat, vdiffr (>= 1.0.2)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## glmnet               "knitr, lars, testthat, xfun, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## globals              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## glue                 "crayon, DBI (>= 1.2.0), dplyr, knitr, magrittr, rlang,\nrmarkdown, RSQLite, testthat (>= 3.2.0), vctrs (>= 0.3.0),\nwaldo (>= 0.5.3), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## gower                "tinytest (>= 0.9.3),"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## graphics             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## grDevices            "KernSmooth"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## grid                 NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## gridExtra            "ggplot2, egg, lattice, knitr, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## gtable               "covr, ggplot2, knitr, profvis, rmarkdown, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## hardhat              "covr, crayon, devtools, knitr, Matrix, modeldata (>= 0.0.2),\nrecipes (>= 1.0.5), rmarkdown (>= 2.3), roxygen2, testthat (>=\n3.0.0), usethis (>= 2.1.5), withr (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## haven                "covr, crayon, fs, knitr, pillar (>= 1.4.0), rmarkdown,\ntestthat (>= 3.0.0), utf8"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## highr                "knitr, markdown, testit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## hms                  "crayon, lubridate, pillar (>= 1.1.0), testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## htmltools            "Cairo, markdown, ragg, shiny, testthat, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## htmlwidgets          "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## httpuv               "callr, curl, jsonlite, testthat, websocket"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## httr                 "covr, httpuv, jpeg, knitr, png, readr, rmarkdown, testthat\n(>= 0.8.0), xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## ipred                "mvtnorm, mlbench, TH.data, randomForest, party"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## IRanges              "XVector, GenomicRanges, Rsamtools, GenomicAlignments,\nGenomicFeatures, BSgenome.Celegans.UCSC.ce2, pasillaBamSubset,\nRUnit, BiocStyle"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## isoband              "covr, ggplot2, knitr, magick, microbenchmark, rmarkdown, sf,\ntestthat, xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## iterators            "RUnit, foreach"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## jquerylib            "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## jsonlite             "httr, vctrs, testthat, knitr, rmarkdown, R.rsp, sf"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## KernSmooth           "MASS, carData"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## knitr                "bslib, codetools, DBI (>= 0.4-1), digest, formatR, gifski,\ngridSVG, htmlwidgets (>= 0.7), jpeg, JuliaCall (>= 0.11.1),\nmagick, litedown, markdown (>= 1.3), png, ragg, reticulate (>=\n1.4), rgl (>= 0.95.1201), rlang, rmarkdown, sass, showtext,\nstyler (>= 1.2.0), targets (>= 0.6.0), testit, tibble,\ntikzDevice (>= 0.10), tinytex (>= 0.56), webshot, rstudioapi,\nsvglite"                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## labeling             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## lambda.r             "testit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## later                "knitr, nanonext, R6, rmarkdown, testthat (>= 2.1.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## lattice              "KernSmooth, MASS, latticeExtra, colorspace"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## lava                 "KernSmooth, Rgraphviz, data.table, ellipse, fields, geepack,\ngraph, knitr, rmarkdown, igraph (>= 0.6), lavaSearch2, lme4 (>=\n1.1.35.1), MASS, Matrix (>= 1.6.3), mets (>= 1.1), nlme,\noptimx, polycor, quantreg, rgl, targeted (>= 0.4), testthat (>=\n0.11), visNetwork"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## lifecycle            "covr, crayon, knitr, lintr, rmarkdown, testthat (>= 3.0.1),\ntibble, tidyverse, tools, vctrs, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## listenv              "R.utils, R.rsp, markdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## lme4                 "knitr, rmarkdown, MEMSS, testthat (>= 0.8.1), ggplot2,\nmlmRev, optimx (>= 2013.8.6), gamm4, pbkrtest, HSAUR3,\nnumDeriv, car, dfoptim, mgcv, statmod, rr2, semEff, tibble,\nmerDeriv"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## lmtest               "car, strucchange, sandwich, dynlm, stats4, survival, AER"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## locfit               "interp, gam"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## lubridate            "covr, knitr, rmarkdown, testthat (>= 2.1.0), vctrs (>= 0.6.5)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## magrittr             "covr, knitr, rlang, rmarkdown, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## MASS                 "lattice, nlme, nnet, survival"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## Matrix               "MASS, datasets, sfsmisc, tools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## MatrixGenerics       "Matrix, sparseMatrixStats, SparseArray, DelayedArray,\nDelayedMatrixStats, SummarizedExperiment, testthat (>= 2.1.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## MatrixModels         NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## matrixStats          "utils, base64enc, ggplot2, knitr, markdown, microbenchmark,\nR.devices, R.rsp"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## memoise              "digest, aws.s3, covr, googleAuthR, googleCloudStorageR, httr,\ntestthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## methods              "codetools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## mgcv                 "parallel, survival, MASS"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## microbenchmark       "ggplot2, multcomp, RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## mime                 NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## miniUI               NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## minqa                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## ModelMetrics         "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## modelr               "compiler, covr, ggplot2, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## moments              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## mvtnorm              "qrng, numDeriv"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## nlme                 "MASS, SASmixed"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## nloptr               "knitr, rmarkdown, covr, tinytest"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## nnet                 "MASS"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## numDeriv             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## openssl              "curl, testthat (>= 2.1.0), digest, knitr, rmarkdown,\njsonlite, jose, sodium"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## parallel             "methods"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## parallelly           "commonmark, base64enc"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## patchwork            "knitr, rmarkdown, gridGraphics, gridExtra, ragg, testthat (>=\n2.1.0), vdiffr, covr, png, gt (>= 0.11.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## pbkrtest             "nlme, markdown, knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## pillar               "bit64, DBI, debugme, DiagrammeR, dplyr, formattable, ggplot2,\nknitr, lubridate, nanotime, nycflights13, palmerpenguins,\nrmarkdown, scales, stringi, survival, testthat (>= 3.1.1),\ntibble, units (>= 0.7.2), vdiffr, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## pkgconfig            "covr, testthat, disposables (>= 1.0.3)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## plotrix              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## plyr                 "abind, covr, doParallel, foreach, iterators, itertools,\ntcltk, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## polynom              "knitr, rmarkdown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## ppcor                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## prettyunits          "codetools, covr, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## pROC                 "microbenchmark, tcltk, MASS, logcondens, doParallel,\ntestthat, vdiffr, ggplot2, rlang"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## processx             "callr (>= 3.7.3), cli (>= 3.3.0), codetools, covr, curl,\ndebugme, parallel, rlang (>= 1.0.2), testthat (>= 3.0.0),\nwebfakes, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## prodlim              "tibble, pammtools, ggthemes"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## progress             "Rcpp, testthat (>= 3.0.0), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## progressr            "graphics, tcltk, beepr, cli, crayon, pbmcapply, progress,\npurrr, foreach, plyr, doFuture, future, future.apply, furrr,\nntfy, RPushbullet, rstudioapi, shiny, commonmark, base64enc,\ntools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## promises             "future (>= 1.21.0), knitr, purrr, rmarkdown, spelling,\ntestthat (>= 3.0.0), vembedr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## proxy                "cba"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## ps                   "callr, covr, curl, pillar, pingr, processx (>= 3.1.0), R6,\nrlang, testthat (>= 3.0.0), webfakes, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## purrr                "carrier (>= 0.2.0), covr, dplyr (>= 0.7.8), httr, knitr,\nlubridate, mirai (>= 2.4.0), rmarkdown, testthat (>= 3.0.0),\ntibble, tidyselect"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## quantreg             "interp, rgl, logspline, nor1mix, Formula, zoo, R.rsp, conquer"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## quarto               "bslib, callr, curl, dplyr, flextable, ggiraph, ggplot2, gt,\nheatmaply, kableExtra, knitr, palmerpenguins, patchwork,\npkgload, plotly, rsconnect (>= 0.8.26), testthat (>= 3.1.7),\nthematic, tidyverse, tinytable, whoami, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## R.methodsS3          "codetools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## R.oo                 "tools"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## R.utils              "datasets, digest (>= 0.6.10)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## R6                   "lobstr, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## rappdirs             "roxygen2, testthat (>= 3.0.0), covr, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## rbibutils            "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## RColorBrewer         NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## Rcpp                 "tinytest, inline, rbenchmark, pkgKitten (>= 0.1.2)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## RcppArmadillo        "tinytest, Matrix (>= 1.3.0), pkgKitten, reticulate, slam"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## RcppEigen            "Matrix, inline, tinytest, pkgKitten, microbenchmark"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## Rdpack               "grDevices, testthat, rstudioapi, rprojroot, gbRd"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## readr                "covr, curl, datasets, knitr, rmarkdown, spelling, stringi,\ntestthat (>= 3.2.0), tzdb (>= 0.1.1), waldo, withr, xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## readxl               "covr, knitr, rmarkdown, testthat (>= 3.1.6), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## recipes              "covr, ddalpha, dials (>= 1.2.0), ggplot2, igraph, kernlab,\nknitr, methods, modeldata (>= 0.1.1), parsnip (>= 1.2.0), RANN,\nRcppRoll, rmarkdown, rpart, rsample, RSpectra, splines2,\ntestthat (>= 3.0.0), workflows, xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## reformulas           "lme4, tinytest, glmmTMB"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## rematch              "covr, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## reshape2             "covr, lattice, testthat (>= 0.8.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## rio                  "datasets, bit64, testthat, knitr, magrittr, clipr, fst,\nhexView, jsonlite, pzfx, readODS (>= 2.1.0), rmarkdown, rmatio,\nxml2 (>= 1.2.0), yaml, qs, arrow (>= 0.17.0), stringi, withr,\nnanoparquet"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## rlang                "cli (>= 3.1.0), covr, crayon, desc, fs, glue, knitr,\nmagrittr, methods, pillar, pkgload, rmarkdown, stats, testthat\n(>= 3.2.0), tibble, usethis, vctrs (>= 0.2.3), withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## rmarkdown            "digest, dygraphs, fs, rsconnect, downlit (>= 0.4.0), katex\n(>= 1.4.0), sass (>= 0.4.0), shiny (>= 1.6.0), testthat (>=\n3.0.3), tibble, vctrs, cleanrmd, withr (>= 2.4.2), xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## rpart                "survival"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## rstatix              "knitr, rmarkdown, ggpubr, graphics, emmeans, coin, boot,\ntestthat, spelling"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    ## rstudioapi           "testthat, knitr, rmarkdown, clipr, covr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## S4Arrays             "BiocParallel, SparseArray (>= 0.0.4), DelayedArray,\nHDF5Array, testthat, knitr, rmarkdown, BiocStyle"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## S4Vectors            "IRanges, GenomicRanges, SummarizedExperiment, Matrix,\nDelayedArray, ShortRead, graph, data.table, RUnit, BiocStyle,\nknitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## sass                 "testthat, knitr, rmarkdown, withr, shiny, curl"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## scales               "bit64, covr, dichromat, ggplot2, hms (>= 0.5.0), stringi,\ntestthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    ## shape                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## shiny                "coro (>= 1.1.0), datasets, DT, Cairo (>= 1.5-5), testthat (>=\n3.2.1), knitr (>= 1.6), markdown, rmarkdown, ggplot2, reactlog\n(>= 1.0.0), magrittr, yaml, mirai, future, dygraphs, ragg,\nshowtext, sass, watcher"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## shinyjs              "htmltools (>= 0.2.9), knitr (>= 1.7), rmarkdown, shinyAce,\nshinydisconnect, testthat (>= 0.9.1)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## snow                 "rlecuyer"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## sourcetools          "testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## SparseArray          "HDF5Array, ExperimentHub, testthat, knitr, rmarkdown,\nBiocStyle"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## SparseM              "knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## sparsevctrs          "knitr, Matrix, methods, rmarkdown, testthat (>= 3.0.0),\ntibble, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## spatial              "MASS"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## splines              "Matrix, methods"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    ## SQUAREM              "setRNG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## stats                "MASS, Matrix, SuppDists, methods, stats4"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    ## stats4               NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## stringi              NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## stringr              "covr, dplyr, gt, htmltools, htmlwidgets, knitr, rmarkdown,\ntestthat (>= 3.0.0), tibble"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## SummarizedExperiment "jsonlite, rhdf5, HDF5Array (>= 1.7.5), annotate,\nAnnotationDbi, GenomicFeatures, SparseArray,\nSingleCellExperiment, TxDb.Hsapiens.UCSC.hg19.knownGene,\nhgu95av2.db, airway (>= 1.15.1), BiocStyle, knitr, rmarkdown,\nRUnit, testthat, digest"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## survival             NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## sys                  "unix (>= 1.4), spelling, testthat"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## tcltk                NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## tibble               "bench, bit64, blob, brio, callr, DiagrammeR, dplyr, evaluate,\nformattable, ggplot2, here, hms, htmltools, knitr, lubridate,\nnycflights13, pkgload, purrr, rmarkdown, stringi, testthat (>=\n3.0.2), tidyr, withr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## tidyr                "covr, data.table, knitr, readr, repurrrsive (>= 1.1.0),\nrmarkdown, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    ## tidyselect           "covr, crayon, dplyr, knitr, magrittr, rmarkdown, stringr,\ntestthat (>= 3.1.1), tibble (>= 2.1.3)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## timechange           "testthat (>= 0.7.1.99), knitr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    ## timeDate             "RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## tinytex              "testit, rstudioapi"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ## titanic              "dplyr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## tools                "codetools, methods, xml2, curl, commonmark, knitr, xfun,\nmathjaxr, V8"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## translations         NA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    ## tzdb                 "covr, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## UCSC.utils           "DBI, RMariaDB, GenomeInfoDb, testthat, knitr, rmarkdown,\nBiocStyle"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## utf8                 "cli, covr, knitr, rlang, rmarkdown, testthat (>= 3.0.0),\nwithr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    ## utils                "methods, xml2, commonmark, knitr, jsonlite"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## vcd                  "KernSmooth, mvtnorm, kernlab, HSAUR3, coin"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    ## vctrs                "bit64, covr, crayon, dplyr (>= 0.8.5), generics, knitr,\npillar (>= 1.4.4), pkgdown (>= 2.0.1), rmarkdown, testthat (>=\n3.0.0), tibble (>= 3.1.3), waldo (>= 0.2.0), withr, xml2,\nzeallot"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    ## viridisLite          "hexbin (>= 1.27.0), ggplot2 (>= 1.0.1), testthat, covr"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    ## vroom                "archive, bench (>= 1.1.0), covr, curl, dplyr, forcats, fs,\nggplot2, knitr, patchwork, prettyunits, purrr, rmarkdown,\nrstudioapi, scales, spelling, testthat (>= 2.1.0), tidyr,\nutils, waldo, xml2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    ## withr                "callr, DBI, knitr, methods, rlang, rmarkdown (>= 2.12),\nRSQLite, testthat (>= 3.0.0)"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## writexl              "spelling, readxl, nycflights13, testthat, bit64"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    ## xfun                 "testit, parallel, codetools, methods, rstudioapi, tinytex (>=\n0.30), mime, litedown (>= 0.4), commonmark, knitr (>= 1.50),\nremotes, pak, curl, xml2, jsonlite, magick, yaml, qs"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    ## xtable               "knitr, plm, zoo, survival"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    ## XVector              "Biostrings, drosophila2probe, RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    ## yaml                 "RUnit"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    ## zoo                  "AER, coda, chron, ggplot2 (>= 3.5.0), mondate, scales,\nstinepack, strucchange, timeDate, timeSeries, tinyplot, tis,\ntseries, xts"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    ##                      Enhances                                                                                          
    ## abind                NA                                                                                                
    ## askpass              NA                                                                                                
    ## backports            NA                                                                                                
    ## base                 "chron, date, round"                                                                              
    ## base64enc            "png"                                                                                             
    ## BH                   NA                                                                                                
    ## Biobase              NA                                                                                                
    ## BiocGenerics         NA                                                                                                
    ## BiocManager          NA                                                                                                
    ## BiocParallel         "Rmpi"                                                                                            
    ## BiocVersion          NA                                                                                                
    ## bit                  NA                                                                                                
    ## bit64                NA                                                                                                
    ## boot                 NA                                                                                                
    ## broom                NA                                                                                                
    ## bslib                NA                                                                                                
    ## cachem               NA                                                                                                
    ## car                  NA                                                                                                
    ## carData              NA                                                                                                
    ## caret                NA                                                                                                
    ## cellranger           NA                                                                                                
    ## class                NA                                                                                                
    ## cli                  NA                                                                                                
    ## clipr                NA                                                                                                
    ## clock                NA                                                                                                
    ## cluster              "mvoutlier, fpc, ellipse, sfsmisc"                                                                
    ## codetools            NA                                                                                                
    ## colorspace           NA                                                                                                
    ## colourpicker         NA                                                                                                
    ## commonmark           NA                                                                                                
    ## compiler             NA                                                                                                
    ## corrplot             NA                                                                                                
    ## cowplot              NA                                                                                                
    ## cpp11                NA                                                                                                
    ## crayon               NA                                                                                                
    ## curl                 NA                                                                                                
    ## data.table           NA                                                                                                
    ## datasets             NA                                                                                                
    ## DelayedArray         NA                                                                                                
    ## Deriv                NA                                                                                                
    ## DESeq2               NA                                                                                                
    ## diagram              NA                                                                                                
    ## digest               NA                                                                                                
    ## doBy                 NA                                                                                                
    ## dplyr                NA                                                                                                
    ## dunn.test            NA                                                                                                
    ## e1071                NA                                                                                                
    ## emmeans              "CARBayes, coxme, gee, geepack, MCMCglmm, MCMCpack, mice,\nnnet, pscl, rstanarm, sommer, survival"
    ## EnhancedVolcano      NA                                                                                                
    ## estimability         NA                                                                                                
    ## evaluate             NA                                                                                                
    ## farver               NA                                                                                                
    ## fastmap              NA                                                                                                
    ## FlexParamCurve       NA                                                                                                
    ## fontawesome          NA                                                                                                
    ## forcats              NA                                                                                                
    ## foreach              NA                                                                                                
    ## foreign              NA                                                                                                
    ## formatR              NA                                                                                                
    ## Formula              NA                                                                                                
    ## fs                   NA                                                                                                
    ## FSA                  NA                                                                                                
    ## futile.logger        NA                                                                                                
    ## futile.options       NA                                                                                                
    ## future               NA                                                                                                
    ## future.apply         NA                                                                                                
    ## generics             NA                                                                                                
    ## GenomeInfoDb         NA                                                                                                
    ## GenomeInfoDbData     NA                                                                                                
    ## GenomicRanges        NA                                                                                                
    ## ggcorrplot           NA                                                                                                
    ## ggExtra              NA                                                                                                
    ## ggplot2              "sp"                                                                                              
    ## ggpubr               NA                                                                                                
    ## ggrepel              NA                                                                                                
    ## ggsci                NA                                                                                                
    ## ggsignif             NA                                                                                                
    ## glmnet               NA                                                                                                
    ## globals              NA                                                                                                
    ## glue                 NA                                                                                                
    ## gower                NA                                                                                                
    ## graphics             "vcd"                                                                                             
    ## grDevices            NA                                                                                                
    ## grid                 NA                                                                                                
    ## gridExtra            NA                                                                                                
    ## gtable               NA                                                                                                
    ## hardhat              NA                                                                                                
    ## haven                NA                                                                                                
    ## highr                NA                                                                                                
    ## hms                  NA                                                                                                
    ## htmltools            "knitr"                                                                                           
    ## htmlwidgets          "shiny (>= 1.1)"                                                                                  
    ## httpuv               NA                                                                                                
    ## httr                 NA                                                                                                
    ## ipred                NA                                                                                                
    ## IRanges              NA                                                                                                
    ## isoband              NA                                                                                                
    ## iterators            NA                                                                                                
    ## jquerylib            NA                                                                                                
    ## jsonlite             NA                                                                                                
    ## KernSmooth           NA                                                                                                
    ## knitr                NA                                                                                                
    ## labeling             NA                                                                                                
    ## lambda.r             NA                                                                                                
    ## later                NA                                                                                                
    ## lattice              "chron, zoo"                                                                                      
    ## lava                 NA                                                                                                
    ## lifecycle            NA                                                                                                
    ## listenv              NA                                                                                                
    ## lme4                 NA                                                                                                
    ## lmtest               NA                                                                                                
    ## locfit               NA                                                                                                
    ## lubridate            "chron, data.table, timeDate, tis, zoo"                                                           
    ## magrittr             NA                                                                                                
    ## MASS                 NA                                                                                                
    ## Matrix               "SparseM, graph"                                                                                  
    ## MatrixGenerics       NA                                                                                                
    ## MatrixModels         NA                                                                                                
    ## matrixStats          NA                                                                                                
    ## memoise              NA                                                                                                
    ## methods              NA                                                                                                
    ## mgcv                 NA                                                                                                
    ## microbenchmark       NA                                                                                                
    ## mime                 NA                                                                                                
    ## miniUI               NA                                                                                                
    ## minqa                NA                                                                                                
    ## ModelMetrics         NA                                                                                                
    ## modelr               NA                                                                                                
    ## moments              NA                                                                                                
    ## mvtnorm              NA                                                                                                
    ## nlme                 NA                                                                                                
    ## nloptr               NA                                                                                                
    ## nnet                 NA                                                                                                
    ## numDeriv             NA                                                                                                
    ## openssl              NA                                                                                                
    ## parallel             "snow, Rmpi, mirai"                                                                               
    ## parallelly           NA                                                                                                
    ## patchwork            NA                                                                                                
    ## pbkrtest             NA                                                                                                
    ## pillar               NA                                                                                                
    ## pkgconfig            NA                                                                                                
    ## plotrix              NA                                                                                                
    ## plyr                 NA                                                                                                
    ## polynom              NA                                                                                                
    ## ppcor                NA                                                                                                
    ## prettyunits          NA                                                                                                
    ## pROC                 NA                                                                                                
    ## processx             NA                                                                                                
    ## prodlim              NA                                                                                                
    ## progress             NA                                                                                                
    ## progressr            NA                                                                                                
    ## promises             NA                                                                                                
    ## proxy                NA                                                                                                
    ## ps                   NA                                                                                                
    ## purrr                NA                                                                                                
    ## quantreg             NA                                                                                                
    ## quarto               NA                                                                                                
    ## R.methodsS3          NA                                                                                                
    ## R.oo                 NA                                                                                                
    ## R.utils              NA                                                                                                
    ## R6                   NA                                                                                                
    ## rappdirs             NA                                                                                                
    ## rbibutils            NA                                                                                                
    ## RColorBrewer         NA                                                                                                
    ## Rcpp                 NA                                                                                                
    ## RcppArmadillo        NA                                                                                                
    ## RcppEigen            NA                                                                                                
    ## Rdpack               NA                                                                                                
    ## readr                NA                                                                                                
    ## readxl               NA                                                                                                
    ## recipes              NA                                                                                                
    ## reformulas           NA                                                                                                
    ## rematch              NA                                                                                                
    ## reshape2             NA                                                                                                
    ## rio                  NA                                                                                                
    ## rlang                "winch"                                                                                           
    ## rmarkdown            NA                                                                                                
    ## rpart                NA                                                                                                
    ## rstatix              NA                                                                                                
    ## rstudioapi           NA                                                                                                
    ## S4Arrays             NA                                                                                                
    ## S4Vectors            NA                                                                                                
    ## sass                 NA                                                                                                
    ## scales               NA                                                                                                
    ## shape                NA                                                                                                
    ## shiny                NA                                                                                                
    ## shinyjs              NA                                                                                                
    ## snow                 "Rmpi"                                                                                            
    ## sourcetools          NA                                                                                                
    ## SparseArray          NA                                                                                                
    ## SparseM              NA                                                                                                
    ## sparsevctrs          NA                                                                                                
    ## spatial              NA                                                                                                
    ## splines              NA                                                                                                
    ## SQUAREM              NA                                                                                                
    ## stats                "Kendall, coin, multcomp, pcaPP, pspearman, robustbase"                                           
    ## stats4               NA                                                                                                
    ## stringi              NA                                                                                                
    ## stringr              NA                                                                                                
    ## SummarizedExperiment NA                                                                                                
    ## survival             NA                                                                                                
    ## sys                  NA                                                                                                
    ## tcltk                NA                                                                                                
    ## tibble               NA                                                                                                
    ## tidyr                NA                                                                                                
    ## tidyselect           NA                                                                                                
    ## timechange           NA                                                                                                
    ## timeDate             NA                                                                                                
    ## tinytex              NA                                                                                                
    ## titanic              NA                                                                                                
    ## tools                NA                                                                                                
    ## translations         NA                                                                                                
    ## tzdb                 NA                                                                                                
    ## UCSC.utils           NA                                                                                                
    ## utf8                 NA                                                                                                
    ## utils                NA                                                                                                
    ## vcd                  NA                                                                                                
    ## vctrs                NA                                                                                                
    ## viridisLite          NA                                                                                                
    ## vroom                NA                                                                                                
    ## withr                NA                                                                                                
    ## writexl              NA                                                                                                
    ## xfun                 NA                                                                                                
    ## xtable               NA                                                                                                
    ## XVector              NA                                                                                                
    ## yaml                 NA                                                                                                
    ## zoo                  NA                                                                                                
    ##                      License                                  License_is_FOSS
    ## abind                "MIT + file LICENSE"                     NA             
    ## askpass              "MIT + file LICENSE"                     NA             
    ## backports            "GPL-2 | GPL-3"                          NA             
    ## base                 "Part of R 4.5.1"                        NA             
    ## base64enc            "GPL-2 | GPL-3"                          NA             
    ## BH                   "BSL-1.0"                                NA             
    ## Biobase              "Artistic-2.0"                           NA             
    ## BiocGenerics         "Artistic-2.0"                           NA             
    ## BiocManager          "Artistic-2.0"                           NA             
    ## BiocParallel         "GPL-2 | GPL-3 | BSL-1.0"                NA             
    ## BiocVersion          "Artistic-2.0"                           NA             
    ## bit                  "GPL-2 | GPL-3"                          NA             
    ## bit64                "GPL-2 | GPL-3"                          NA             
    ## boot                 "Unlimited"                              NA             
    ## broom                "MIT + file LICENSE"                     NA             
    ## bslib                "MIT + file LICENSE"                     NA             
    ## cachem               "MIT + file LICENSE"                     NA             
    ## car                  "GPL (>= 2)"                             NA             
    ## carData              "GPL (>= 2)"                             NA             
    ## caret                "GPL (>= 2)"                             NA             
    ## cellranger           "MIT + file LICENSE"                     NA             
    ## class                "GPL-2 | GPL-3"                          NA             
    ## cli                  "MIT + file LICENSE"                     NA             
    ## clipr                "GPL-3"                                  NA             
    ## clock                "MIT + file LICENSE"                     NA             
    ## cluster              "GPL (>= 2)"                             NA             
    ## codetools            "GPL"                                    NA             
    ## colorspace           "BSD_3_clause + file LICENSE"            NA             
    ## colourpicker         "MIT + file LICENSE"                     NA             
    ## commonmark           "BSD_2_clause + file LICENSE"            NA             
    ## compiler             "Part of R 4.5.1"                        NA             
    ## corrplot             "MIT + file LICENSE"                     NA             
    ## cowplot              "GPL-2"                                  NA             
    ## cpp11                "MIT + file LICENSE"                     NA             
    ## crayon               "MIT + file LICENSE"                     NA             
    ## curl                 "MIT + file LICENSE"                     NA             
    ## data.table           "MPL-2.0 | file LICENSE"                 NA             
    ## datasets             "Part of R 4.5.1"                        NA             
    ## DelayedArray         "Artistic-2.0"                           NA             
    ## Deriv                "GPL (>= 3)"                             NA             
    ## DESeq2               "LGPL (>= 3)"                            NA             
    ## diagram              "GPL (>= 2)"                             NA             
    ## digest               "GPL (>= 2)"                             NA             
    ## doBy                 "GPL (>= 2)"                             NA             
    ## dplyr                "MIT + file LICENSE"                     NA             
    ## dunn.test            "GPL-2"                                  NA             
    ## e1071                "GPL-2 | GPL-3"                          NA             
    ## emmeans              "GPL-2 | GPL-3"                          NA             
    ## EnhancedVolcano      "GPL-3"                                  NA             
    ## estimability         "GPL (>= 3)"                             NA             
    ## evaluate             "MIT + file LICENSE"                     NA             
    ## farver               "MIT + file LICENSE"                     NA             
    ## fastmap              "MIT + file LICENSE"                     NA             
    ## FlexParamCurve       "GPL-2"                                  NA             
    ## fontawesome          "MIT + file LICENSE"                     NA             
    ## forcats              "MIT + file LICENSE"                     NA             
    ## foreach              "Apache License (== 2.0)"                NA             
    ## foreign              "GPL (>= 2)"                             NA             
    ## formatR              "GPL"                                    NA             
    ## Formula              "GPL-2 | GPL-3"                          NA             
    ## fs                   "MIT + file LICENSE"                     NA             
    ## FSA                  "GPL (>= 2)"                             NA             
    ## futile.logger        "LGPL-3"                                 NA             
    ## futile.options       "LGPL-3"                                 NA             
    ## future               "LGPL (>= 2.1)"                          NA             
    ## future.apply         "GPL (>= 2)"                             NA             
    ## generics             "MIT + file LICENSE"                     NA             
    ## GenomeInfoDb         "Artistic-2.0"                           NA             
    ## GenomeInfoDbData     "Artistic-2.0"                           NA             
    ## GenomicRanges        "Artistic-2.0"                           NA             
    ## ggcorrplot           "GPL-2"                                  NA             
    ## ggExtra              "MIT + file LICENSE"                     NA             
    ## ggplot2              "MIT + file LICENSE"                     NA             
    ## ggpubr               "GPL (>= 2)"                             NA             
    ## ggrepel              "GPL-3 | file LICENSE"                   NA             
    ## ggsci                "GPL (>= 3)"                             NA             
    ## ggsignif             "GPL-3 | file LICENSE"                   NA             
    ## glmnet               "GPL-2"                                  NA             
    ## globals              "LGPL (>= 2.1)"                          NA             
    ## glue                 "MIT + file LICENSE"                     NA             
    ## gower                "GPL-3"                                  NA             
    ## graphics             "Part of R 4.5.1"                        NA             
    ## grDevices            "Part of R 4.5.1"                        NA             
    ## grid                 "Part of R 4.5.1"                        NA             
    ## gridExtra            "GPL (>= 2)"                             NA             
    ## gtable               "MIT + file LICENSE"                     NA             
    ## hardhat              "MIT + file LICENSE"                     NA             
    ## haven                "MIT + file LICENSE"                     NA             
    ## highr                "GPL"                                    NA             
    ## hms                  "MIT + file LICENSE"                     NA             
    ## htmltools            "GPL (>= 2)"                             NA             
    ## htmlwidgets          "MIT + file LICENSE"                     NA             
    ## httpuv               "GPL (>= 2) | file LICENSE"              NA             
    ## httr                 "MIT + file LICENSE"                     NA             
    ## ipred                "GPL (>= 2)"                             NA             
    ## IRanges              "Artistic-2.0"                           NA             
    ## isoband              "MIT + file LICENSE"                     NA             
    ## iterators            "Apache License (== 2.0)"                NA             
    ## jquerylib            "MIT + file LICENSE"                     NA             
    ## jsonlite             "MIT + file LICENSE"                     NA             
    ## KernSmooth           "Unlimited"                              NA             
    ## knitr                "GPL"                                    NA             
    ## labeling             "MIT + file LICENSE | Unlimited"         NA             
    ## lambda.r             "LGPL-3"                                 NA             
    ## later                "MIT + file LICENSE"                     NA             
    ## lattice              "GPL (>= 2)"                             NA             
    ## lava                 "GPL-3"                                  NA             
    ## lifecycle            "MIT + file LICENSE"                     NA             
    ## listenv              "LGPL (>= 2.1)"                          NA             
    ## lme4                 "GPL (>= 2)"                             NA             
    ## lmtest               "GPL-2 | GPL-3"                          NA             
    ## locfit               "GPL (>= 2)"                             NA             
    ## lubridate            "GPL (>= 2)"                             NA             
    ## magrittr             "MIT + file LICENSE"                     NA             
    ## MASS                 "GPL-2 | GPL-3"                          NA             
    ## Matrix               "GPL (>= 2) | file LICENCE"              NA             
    ## MatrixGenerics       "Artistic-2.0"                           NA             
    ## MatrixModels         "GPL (>= 2)"                             NA             
    ## matrixStats          "Artistic-2.0"                           NA             
    ## memoise              "MIT + file LICENSE"                     NA             
    ## methods              "Part of R 4.5.1"                        NA             
    ## mgcv                 "GPL (>= 2)"                             NA             
    ## microbenchmark       "BSD_2_clause + file LICENSE"            NA             
    ## mime                 "GPL"                                    NA             
    ## miniUI               "GPL-3"                                  NA             
    ## minqa                "GPL-2"                                  NA             
    ## ModelMetrics         "GPL (>= 2)"                             NA             
    ## modelr               "GPL-3"                                  NA             
    ## moments              "GPL (>= 2)"                             NA             
    ## mvtnorm              "GPL-2"                                  NA             
    ## nlme                 "GPL (>= 2)"                             NA             
    ## nloptr               "LGPL (>= 3)"                            NA             
    ## nnet                 "GPL-2 | GPL-3"                          NA             
    ## numDeriv             "GPL-2"                                  NA             
    ## openssl              "MIT + file LICENSE"                     NA             
    ## parallel             "Part of R 4.5.1"                        NA             
    ## parallelly           "LGPL (>= 2.1)"                          NA             
    ## patchwork            "MIT + file LICENSE"                     NA             
    ## pbkrtest             "GPL (>= 2)"                             NA             
    ## pillar               "MIT + file LICENSE"                     NA             
    ## pkgconfig            "MIT + file LICENSE"                     NA             
    ## plotrix              "GPL (>= 2)"                             NA             
    ## plyr                 "MIT + file LICENSE"                     NA             
    ## polynom              "GPL-2"                                  NA             
    ## ppcor                "GPL-2"                                  NA             
    ## prettyunits          "MIT + file LICENSE"                     NA             
    ## pROC                 "GPL (>= 3)"                             NA             
    ## processx             "MIT + file LICENSE"                     NA             
    ## prodlim              "GPL (>= 2)"                             NA             
    ## progress             "MIT + file LICENSE"                     NA             
    ## progressr            "GPL (>= 3)"                             NA             
    ## promises             "MIT + file LICENSE"                     NA             
    ## proxy                "GPL-2"                                  NA             
    ## ps                   "MIT + file LICENSE"                     NA             
    ## purrr                "MIT + file LICENSE"                     NA             
    ## quantreg             "GPL (>= 2)"                             NA             
    ## quarto               "MIT + file LICENSE"                     NA             
    ## R.methodsS3          "LGPL (>= 2.1)"                          NA             
    ## R.oo                 "LGPL (>= 2.1)"                          NA             
    ## R.utils              "LGPL (>= 2.1)"                          NA             
    ## R6                   "MIT + file LICENSE"                     NA             
    ## rappdirs             "MIT + file LICENSE"                     NA             
    ## rbibutils            "GPL-2"                                  NA             
    ## RColorBrewer         "Apache License 2.0"                     NA             
    ## Rcpp                 "GPL (>= 2)"                             NA             
    ## RcppArmadillo        "GPL (>= 2)"                             NA             
    ## RcppEigen            "GPL (>= 2) | file LICENSE"              NA             
    ## Rdpack               "GPL (>= 2)"                             NA             
    ## readr                "MIT + file LICENSE"                     NA             
    ## readxl               "MIT + file LICENSE"                     NA             
    ## recipes              "MIT + file LICENSE"                     NA             
    ## reformulas           "GPL-3"                                  NA             
    ## rematch              "MIT + file LICENSE"                     NA             
    ## reshape2             "MIT + file LICENSE"                     NA             
    ## rio                  "GPL-2"                                  NA             
    ## rlang                "MIT + file LICENSE"                     NA             
    ## rmarkdown            "GPL-3"                                  NA             
    ## rpart                "GPL-2 | GPL-3"                          NA             
    ## rstatix              "GPL-2"                                  NA             
    ## rstudioapi           "MIT + file LICENSE"                     NA             
    ## S4Arrays             "Artistic-2.0"                           NA             
    ## S4Vectors            "Artistic-2.0"                           NA             
    ## sass                 "MIT + file LICENSE"                     NA             
    ## scales               "MIT + file LICENSE"                     NA             
    ## shape                "GPL (>= 3)"                             NA             
    ## shiny                "GPL-3 | file LICENSE"                   NA             
    ## shinyjs              "MIT + file LICENSE"                     NA             
    ## snow                 "GPL"                                    NA             
    ## sourcetools          "MIT + file LICENSE"                     NA             
    ## SparseArray          "Artistic-2.0"                           NA             
    ## SparseM              "GPL (>= 2)"                             NA             
    ## sparsevctrs          "MIT + file LICENSE"                     NA             
    ## spatial              "GPL-2 | GPL-3"                          NA             
    ## splines              "Part of R 4.5.1"                        NA             
    ## SQUAREM              "GPL (>= 2)"                             NA             
    ## stats                "Part of R 4.5.1"                        NA             
    ## stats4               "Part of R 4.5.1"                        NA             
    ## stringi              "file LICENSE"                           "yes"          
    ## stringr              "MIT + file LICENSE"                     NA             
    ## SummarizedExperiment "Artistic-2.0"                           NA             
    ## survival             "LGPL (>= 2)"                            NA             
    ## sys                  "MIT + file LICENSE"                     NA             
    ## tcltk                "Part of R 4.5.1"                        NA             
    ## tibble               "MIT + file LICENSE"                     NA             
    ## tidyr                "MIT + file LICENSE"                     NA             
    ## tidyselect           "MIT + file LICENSE"                     NA             
    ## timechange           "GPL (>= 3)"                             NA             
    ## timeDate             "GPL (>= 2)"                             NA             
    ## tinytex              "MIT + file LICENSE"                     NA             
    ## titanic              "CC0"                                    NA             
    ## tools                "Part of R 4.5.1"                        NA             
    ## translations         "Part of R 4.5.1"                        NA             
    ## tzdb                 "MIT + file LICENSE"                     NA             
    ## UCSC.utils           "Artistic-2.0"                           NA             
    ## utf8                 "Apache License (== 2.0) | file LICENSE" NA             
    ## utils                "Part of R 4.5.1"                        NA             
    ## vcd                  "GPL-2"                                  NA             
    ## vctrs                "MIT + file LICENSE"                     NA             
    ## viridisLite          "MIT + file LICENSE"                     NA             
    ## vroom                "MIT + file LICENSE"                     NA             
    ## withr                "MIT + file LICENSE"                     NA             
    ## writexl              "BSD_2_clause + file LICENSE"            NA             
    ## xfun                 "MIT + file LICENSE"                     NA             
    ## xtable               "GPL (>= 2)"                             NA             
    ## XVector              "Artistic-2.0"                           NA             
    ## yaml                 "BSD_3_clause + file LICENSE"            NA             
    ## zoo                  "GPL-2 | GPL-3"                          NA             
    ##                      License_restricts_use OS_type MD5sum NeedsCompilation
    ## abind                NA                    NA      NA     "no"            
    ## askpass              NA                    NA      NA     "yes"           
    ## backports            NA                    NA      NA     "yes"           
    ## base                 NA                    NA      NA     NA              
    ## base64enc            NA                    NA      NA     "yes"           
    ## BH                   NA                    NA      NA     "no"            
    ## Biobase              NA                    NA      NA     "yes"           
    ## BiocGenerics         NA                    NA      NA     "no"            
    ## BiocManager          NA                    NA      NA     "no"            
    ## BiocParallel         NA                    NA      NA     "yes"           
    ## BiocVersion          NA                    NA      NA     "no"            
    ## bit                  NA                    NA      NA     "yes"           
    ## bit64                NA                    NA      NA     "yes"           
    ## boot                 NA                    NA      NA     "no"            
    ## broom                NA                    NA      NA     "no"            
    ## bslib                NA                    NA      NA     "no"            
    ## cachem               NA                    NA      NA     "yes"           
    ## car                  NA                    NA      NA     "no"            
    ## carData              NA                    NA      NA     "no"            
    ## caret                NA                    NA      NA     "yes"           
    ## cellranger           NA                    NA      NA     "no"            
    ## class                NA                    NA      NA     "yes"           
    ## cli                  NA                    NA      NA     "yes"           
    ## clipr                NA                    NA      NA     "no"            
    ## clock                NA                    NA      NA     "yes"           
    ## cluster              NA                    NA      NA     "yes"           
    ## codetools            NA                    NA      NA     "no"            
    ## colorspace           NA                    NA      NA     "yes"           
    ## colourpicker         NA                    NA      NA     "no"            
    ## commonmark           NA                    NA      NA     "yes"           
    ## compiler             NA                    NA      NA     NA              
    ## corrplot             NA                    NA      NA     "no"            
    ## cowplot              NA                    NA      NA     "no"            
    ## cpp11                NA                    NA      NA     "no"            
    ## crayon               NA                    NA      NA     "no"            
    ## curl                 NA                    NA      NA     "yes"           
    ## data.table           NA                    NA      NA     "yes"           
    ## datasets             NA                    NA      NA     NA              
    ## DelayedArray         NA                    NA      NA     "yes"           
    ## Deriv                NA                    NA      NA     "no"            
    ## DESeq2               NA                    NA      NA     "yes"           
    ## diagram              NA                    NA      NA     "no"            
    ## digest               NA                    NA      NA     "yes"           
    ## doBy                 NA                    NA      NA     "no"            
    ## dplyr                NA                    NA      NA     "yes"           
    ## dunn.test            NA                    NA      NA     "no"            
    ## e1071                NA                    NA      NA     "yes"           
    ## emmeans              NA                    NA      NA     "no"            
    ## EnhancedVolcano      NA                    NA      NA     "no"            
    ## estimability         NA                    NA      NA     "no"            
    ## evaluate             NA                    NA      NA     "no"            
    ## farver               NA                    NA      NA     "yes"           
    ## fastmap              NA                    NA      NA     "yes"           
    ## FlexParamCurve       NA                    NA      NA     "no"            
    ## fontawesome          NA                    NA      NA     "no"            
    ## forcats              NA                    NA      NA     "no"            
    ## foreach              NA                    NA      NA     "no"            
    ## foreign              NA                    NA      NA     "yes"           
    ## formatR              NA                    NA      NA     "no"            
    ## Formula              NA                    NA      NA     "no"            
    ## fs                   NA                    NA      NA     "yes"           
    ## FSA                  NA                    NA      NA     "no"            
    ## futile.logger        NA                    NA      NA     "no"            
    ## futile.options       NA                    NA      NA     "no"            
    ## future               NA                    NA      NA     "no"            
    ## future.apply         NA                    NA      NA     "no"            
    ## generics             NA                    NA      NA     "no"            
    ## GenomeInfoDb         NA                    NA      NA     "no"            
    ## GenomeInfoDbData     NA                    NA      NA     "no"            
    ## GenomicRanges        NA                    NA      NA     "yes"           
    ## ggcorrplot           NA                    NA      NA     "no"            
    ## ggExtra              NA                    NA      NA     "no"            
    ## ggplot2              NA                    NA      NA     "no"            
    ## ggpubr               NA                    NA      NA     "no"            
    ## ggrepel              NA                    NA      NA     "yes"           
    ## ggsci                NA                    NA      NA     "no"            
    ## ggsignif             NA                    NA      NA     "no"            
    ## glmnet               NA                    NA      NA     "yes"           
    ## globals              NA                    NA      NA     "no"            
    ## glue                 NA                    NA      NA     "yes"           
    ## gower                NA                    NA      NA     "yes"           
    ## graphics             NA                    NA      NA     "yes"           
    ## grDevices            NA                    NA      NA     "yes"           
    ## grid                 NA                    NA      NA     "yes"           
    ## gridExtra            NA                    NA      NA     "no"            
    ## gtable               NA                    NA      NA     "no"            
    ## hardhat              NA                    NA      NA     "no"            
    ## haven                NA                    NA      NA     "yes"           
    ## highr                NA                    NA      NA     "no"            
    ## hms                  NA                    NA      NA     "no"            
    ## htmltools            NA                    NA      NA     "yes"           
    ## htmlwidgets          NA                    NA      NA     "no"            
    ## httpuv               NA                    NA      NA     "yes"           
    ## httr                 NA                    NA      NA     "no"            
    ## ipred                NA                    NA      NA     "yes"           
    ## IRanges              NA                    NA      NA     "yes"           
    ## isoband              NA                    NA      NA     "yes"           
    ## iterators            NA                    NA      NA     "no"            
    ## jquerylib            NA                    NA      NA     "no"            
    ## jsonlite             NA                    NA      NA     "yes"           
    ## KernSmooth           NA                    NA      NA     "yes"           
    ## knitr                NA                    NA      NA     "no"            
    ## labeling             NA                    NA      NA     "no"            
    ## lambda.r             NA                    NA      NA     "no"            
    ## later                NA                    NA      NA     "yes"           
    ## lattice              NA                    NA      NA     "yes"           
    ## lava                 NA                    NA      NA     "no"            
    ## lifecycle            NA                    NA      NA     "no"            
    ## listenv              NA                    NA      NA     "no"            
    ## lme4                 NA                    NA      NA     "yes"           
    ## lmtest               NA                    NA      NA     "yes"           
    ## locfit               NA                    NA      NA     "yes"           
    ## lubridate            NA                    NA      NA     "yes"           
    ## magrittr             NA                    NA      NA     "yes"           
    ## MASS                 NA                    NA      NA     "yes"           
    ## Matrix               NA                    NA      NA     "yes"           
    ## MatrixGenerics       NA                    NA      NA     "no"            
    ## MatrixModels         NA                    NA      NA     "no"            
    ## matrixStats          NA                    NA      NA     "yes"           
    ## memoise              NA                    NA      NA     "no"            
    ## methods              NA                    NA      NA     "yes"           
    ## mgcv                 NA                    NA      NA     "yes"           
    ## microbenchmark       NA                    NA      NA     "yes"           
    ## mime                 NA                    NA      NA     "yes"           
    ## miniUI               NA                    NA      NA     "no"            
    ## minqa                NA                    NA      NA     "yes"           
    ## ModelMetrics         NA                    NA      NA     "yes"           
    ## modelr               NA                    NA      NA     "no"            
    ## moments              NA                    NA      NA     "no"            
    ## mvtnorm              NA                    NA      NA     "yes"           
    ## nlme                 NA                    NA      NA     "yes"           
    ## nloptr               NA                    NA      NA     "yes"           
    ## nnet                 NA                    NA      NA     "yes"           
    ## numDeriv             NA                    NA      NA     "no"            
    ## openssl              NA                    NA      NA     "yes"           
    ## parallel             NA                    NA      NA     "yes"           
    ## parallelly           NA                    NA      NA     "yes"           
    ## patchwork            NA                    NA      NA     "no"            
    ## pbkrtest             NA                    NA      NA     "no"            
    ## pillar               NA                    NA      NA     "no"            
    ## pkgconfig            NA                    NA      NA     "no"            
    ## plotrix              NA                    NA      NA     "no"            
    ## plyr                 NA                    NA      NA     "yes"           
    ## polynom              NA                    NA      NA     "no"            
    ## ppcor                NA                    NA      NA     "no"            
    ## prettyunits          NA                    NA      NA     "no"            
    ## pROC                 NA                    NA      NA     "yes"           
    ## processx             NA                    NA      NA     "yes"           
    ## prodlim              NA                    NA      NA     "yes"           
    ## progress             NA                    NA      NA     "no"            
    ## progressr            NA                    NA      NA     "no"            
    ## promises             NA                    NA      NA     "yes"           
    ## proxy                NA                    NA      NA     "yes"           
    ## ps                   NA                    NA      NA     "yes"           
    ## purrr                NA                    NA      NA     "yes"           
    ## quantreg             NA                    NA      NA     "yes"           
    ## quarto               NA                    NA      NA     "no"            
    ## R.methodsS3          NA                    NA      NA     "no"            
    ## R.oo                 NA                    NA      NA     "no"            
    ## R.utils              NA                    NA      NA     "no"            
    ## R6                   NA                    NA      NA     "no"            
    ## rappdirs             NA                    NA      NA     "yes"           
    ## rbibutils            NA                    NA      NA     "yes"           
    ## RColorBrewer         NA                    NA      NA     "no"            
    ## Rcpp                 NA                    NA      NA     "yes"           
    ## RcppArmadillo        NA                    NA      NA     "yes"           
    ## RcppEigen            NA                    NA      NA     "yes"           
    ## Rdpack               NA                    NA      NA     "no"            
    ## readr                NA                    NA      NA     "yes"           
    ## readxl               NA                    NA      NA     "yes"           
    ## recipes              NA                    NA      NA     "no"            
    ## reformulas           NA                    NA      NA     "no"            
    ## rematch              NA                    NA      NA     "no"            
    ## reshape2             NA                    NA      NA     "yes"           
    ## rio                  NA                    NA      NA     "no"            
    ## rlang                NA                    NA      NA     "yes"           
    ## rmarkdown            NA                    NA      NA     "no"            
    ## rpart                NA                    NA      NA     "yes"           
    ## rstatix              NA                    NA      NA     "no"            
    ## rstudioapi           NA                    NA      NA     "no"            
    ## S4Arrays             NA                    NA      NA     "yes"           
    ## S4Vectors            NA                    NA      NA     "yes"           
    ## sass                 NA                    NA      NA     "yes"           
    ## scales               NA                    NA      NA     "no"            
    ## shape                NA                    NA      NA     "no"            
    ## shiny                NA                    NA      NA     "no"            
    ## shinyjs              NA                    NA      NA     "no"            
    ## snow                 NA                    NA      NA     "no"            
    ## sourcetools          NA                    NA      NA     "yes"           
    ## SparseArray          NA                    NA      NA     "yes"           
    ## SparseM              NA                    NA      NA     "yes"           
    ## sparsevctrs          NA                    NA      NA     "yes"           
    ## spatial              NA                    NA      NA     "yes"           
    ## splines              NA                    NA      NA     "yes"           
    ## SQUAREM              NA                    NA      NA     "no"            
    ## stats                NA                    NA      NA     "yes"           
    ## stats4               NA                    NA      NA     NA              
    ## stringi              NA                    NA      NA     "yes"           
    ## stringr              NA                    NA      NA     "no"            
    ## SummarizedExperiment NA                    NA      NA     "no"            
    ## survival             NA                    NA      NA     "yes"           
    ## sys                  NA                    NA      NA     "yes"           
    ## tcltk                NA                    NA      NA     "yes"           
    ## tibble               NA                    NA      NA     "yes"           
    ## tidyr                NA                    NA      NA     "yes"           
    ## tidyselect           NA                    NA      NA     "yes"           
    ## timechange           NA                    NA      NA     "yes"           
    ## timeDate             NA                    NA      NA     "no"            
    ## tinytex              NA                    NA      NA     "no"            
    ## titanic              NA                    NA      NA     "no"            
    ## tools                NA                    NA      NA     "yes"           
    ## translations         NA                    NA      NA     NA              
    ## tzdb                 NA                    NA      NA     "yes"           
    ## UCSC.utils           NA                    NA      NA     "no"            
    ## utf8                 NA                    NA      NA     "yes"           
    ## utils                NA                    NA      NA     "yes"           
    ## vcd                  NA                    NA      NA     "no"            
    ## vctrs                NA                    NA      NA     "yes"           
    ## viridisLite          NA                    NA      NA     "no"            
    ## vroom                NA                    NA      NA     "yes"           
    ## withr                NA                    NA      NA     "no"            
    ## writexl              NA                    NA      NA     "yes"           
    ## xfun                 NA                    NA      NA     "yes"           
    ## xtable               NA                    NA      NA     "no"            
    ## XVector              NA                    NA      NA     "yes"           
    ## yaml                 NA                    NA      NA     "yes"           
    ## zoo                  NA                    NA      NA     "yes"           
    ##                      Built  
    ## abind                "4.5.0"
    ## askpass              "4.5.1"
    ## backports            "4.5.0"
    ## base                 "4.5.1"
    ## base64enc            "4.5.0"
    ## BH                   "4.5.0"
    ## Biobase              "4.5.0"
    ## BiocGenerics         "4.5.0"
    ## BiocManager          "4.5.1"
    ## BiocParallel         "4.5.0"
    ## BiocVersion          "4.5.0"
    ## bit                  "4.5.1"
    ## bit64                "4.5.1"
    ## boot                 "4.5.1"
    ## broom                "4.5.1"
    ## bslib                "4.5.1"
    ## cachem               "4.5.1"
    ## car                  "4.5.1"
    ## carData              "4.5.1"
    ## caret                "4.5.1"
    ## cellranger           "4.5.1"
    ## class                "4.5.1"
    ## cli                  "4.5.1"
    ## clipr                "4.5.1"
    ## clock                "4.5.1"
    ## cluster              "4.5.1"
    ## codetools            "4.5.1"
    ## colorspace           "4.5.1"
    ## colourpicker         "4.5.1"
    ## commonmark           "4.5.1"
    ## compiler             "4.5.1"
    ## corrplot             "4.5.1"
    ## cowplot              "4.5.1"
    ## cpp11                "4.5.1"
    ## crayon               "4.5.1"
    ## curl                 "4.5.1"
    ## data.table           "4.5.1"
    ## datasets             "4.5.1"
    ## DelayedArray         "4.5.0"
    ## Deriv                "4.5.1"
    ## DESeq2               "4.5.0"
    ## diagram              "4.5.0"
    ## digest               "4.5.1"
    ## doBy                 "4.5.1"
    ## dplyr                "4.5.1"
    ## dunn.test            "4.5.0"
    ## e1071                "4.5.1"
    ## emmeans              "4.5.1"
    ## EnhancedVolcano      "4.5.0"
    ## estimability         "4.5.1"
    ## evaluate             "4.5.1"
    ## farver               "4.5.1"
    ## fastmap              "4.5.1"
    ## FlexParamCurve       "4.5.1"
    ## fontawesome          "4.5.1"
    ## forcats              "4.5.1"
    ## foreach              "4.5.1"
    ## foreign              "4.5.1"
    ## formatR              "4.5.1"
    ## Formula              "4.5.0"
    ## fs                   "4.5.1"
    ## FSA                  "4.5.1"
    ## futile.logger        "4.5.1"
    ## futile.options       "4.5.0"
    ## future               "4.5.1"
    ## future.apply         "4.5.1"
    ## generics             "4.5.1"
    ## GenomeInfoDb         "4.5.0"
    ## GenomeInfoDbData     "4.5.1"
    ## GenomicRanges        "4.5.0"
    ## ggcorrplot           "4.5.1"
    ## ggExtra              "4.5.1"
    ## ggplot2              "4.5.1"
    ## ggpubr               "4.5.1"
    ## ggrepel              "4.5.1"
    ## ggsci                "4.5.1"
    ## ggsignif             "4.5.1"
    ## glmnet               "4.5.1"
    ## globals              "4.5.0"
    ## glue                 "4.5.1"
    ## gower                "4.5.0"
    ## graphics             "4.5.1"
    ## grDevices            "4.5.1"
    ## grid                 "4.5.1"
    ## gridExtra            "4.5.1"
    ## gtable               "4.5.1"
    ## hardhat              "4.5.1"
    ## haven                "4.5.1"
    ## highr                "4.5.1"
    ## hms                  "4.5.1"
    ## htmltools            "4.5.1"
    ## htmlwidgets          "4.5.1"
    ## httpuv               "4.5.1"
    ## httr                 "4.5.1"
    ## ipred                "4.5.1"
    ## IRanges              "4.5.0"
    ## isoband              "4.5.1"
    ## iterators            "4.5.1"
    ## jquerylib            "4.5.1"
    ## jsonlite             "4.5.1"
    ## KernSmooth           "4.5.1"
    ## knitr                "4.5.1"
    ## labeling             "4.5.0"
    ## lambda.r             "4.5.1"
    ## later                "4.5.1"
    ## lattice              "4.5.1"
    ## lava                 "4.5.1"
    ## lifecycle            "4.5.1"
    ## listenv              "4.5.1"
    ## lme4                 "4.5.1"
    ## lmtest               "4.5.1"
    ## locfit               "4.5.1"
    ## lubridate            "4.5.1"
    ## magrittr             "4.5.1"
    ## MASS                 "4.5.1"
    ## Matrix               "4.5.1"
    ## MatrixGenerics       "4.5.0"
    ## MatrixModels         "4.5.1"
    ## matrixStats          "4.5.1"
    ## memoise              "4.5.1"
    ## methods              "4.5.1"
    ## mgcv                 "4.5.1"
    ## microbenchmark       "4.5.1"
    ## mime                 "4.5.0"
    ## miniUI               "4.5.1"
    ## minqa                "4.5.1"
    ## ModelMetrics         "4.5.1"
    ## modelr               "4.5.1"
    ## moments              "4.5.0"
    ## mvtnorm              "4.5.1"
    ## nlme                 "4.5.1"
    ## nloptr               "4.5.1"
    ## nnet                 "4.5.1"
    ## numDeriv             "4.5.0"
    ## openssl              "4.5.1"
    ## parallel             "4.5.1"
    ## parallelly           "4.5.1"
    ## patchwork            "4.5.1"
    ## pbkrtest             "4.5.1"
    ## pillar               "4.5.1"
    ## pkgconfig            "4.5.1"
    ## plotrix              "4.5.0"
    ## plyr                 "4.5.1"
    ## polynom              "4.5.1"
    ## ppcor                "4.5.1"
    ## prettyunits          "4.5.1"
    ## pROC                 "4.5.1"
    ## processx             "4.5.1"
    ## prodlim              "4.5.1"
    ## progress             "4.5.1"
    ## progressr            "4.5.1"
    ## promises             "4.5.1"
    ## proxy                "4.5.1"
    ## ps                   "4.5.1"
    ## purrr                "4.5.1"
    ## quantreg             "4.5.1"
    ## quarto               "4.5.1"
    ## R.methodsS3          "4.5.0"
    ## R.oo                 "4.5.0"
    ## R.utils              "4.5.1"
    ## R6                   "4.5.1"
    ## rappdirs             "4.5.1"
    ## rbibutils            "4.5.1"
    ## RColorBrewer         "4.5.0"
    ## Rcpp                 "4.5.1"
    ## RcppArmadillo        "4.5.1"
    ## RcppEigen            "4.5.1"
    ## Rdpack               "4.5.1"
    ## readr                "4.5.1"
    ## readxl               "4.5.1"
    ## recipes              "4.5.1"
    ## reformulas           "4.5.1"
    ## rematch              "4.5.1"
    ## reshape2             "4.5.1"
    ## rio                  "4.5.1"
    ## rlang                "4.5.1"
    ## rmarkdown            "4.5.1"
    ## rpart                "4.5.1"
    ## rstatix              "4.5.1"
    ## rstudioapi           "4.5.1"
    ## S4Arrays             "4.5.0"
    ## S4Vectors            "4.5.0"
    ## sass                 "4.5.1"
    ## scales               "4.5.1"
    ## shape                "4.5.0"
    ## shiny                "4.5.1"
    ## shinyjs              "4.5.1"
    ## snow                 "4.5.0"
    ## sourcetools          "4.5.1"
    ## SparseArray          "4.5.0"
    ## SparseM              "4.5.1"
    ## sparsevctrs          "4.5.1"
    ## spatial              "4.5.1"
    ## splines              "4.5.1"
    ## SQUAREM              "4.5.0"
    ## stats                "4.5.1"
    ## stats4               "4.5.1"
    ## stringi              "4.5.0"
    ## stringr              "4.5.1"
    ## SummarizedExperiment "4.5.0"
    ## survival             "4.5.1"
    ## sys                  "4.5.1"
    ## tcltk                "4.5.1"
    ## tibble               "4.5.1"
    ## tidyr                "4.5.1"
    ## tidyselect           "4.5.1"
    ## timechange           "4.5.1"
    ## timeDate             "4.5.0"
    ## tinytex              "4.5.1"
    ## titanic              "4.5.1"
    ## tools                "4.5.1"
    ## translations         "4.5.1"
    ## tzdb                 "4.5.1"
    ## UCSC.utils           "4.5.0"
    ## utf8                 "4.5.1"
    ## utils                "4.5.1"
    ## vcd                  "4.5.1"
    ## vctrs                "4.5.1"
    ## viridisLite          "4.5.1"
    ## vroom                "4.5.1"
    ## withr                "4.5.1"
    ## writexl              "4.5.1"
    ## xfun                 "4.5.1"
    ## xtable               "4.5.1"
    ## XVector              "4.5.0"
    ## yaml                 "4.5.0"
    ## zoo                  "4.5.1"

    help(package="ggplot2")  # help(package("包的名字”)查看包的功能

## 2、R的基本数据结构

一些基本的数据知识

    # 字符串变量
    a_str <- 'Rstudio'

    # 数字变量
    a_numb <- 23

    # 逻辑型变量
    a_logi <- TRUE
    a_F <- FALSE

数据类型、结构的查看

    # 查看数据大类，character、numeric、logical
    # mode()

    # 查看数据细类，integer、double、single、float
    # typeof()

    # 查看变量类型，vector、data.frame、matrix、factor、list
    # class()

### 2.1 向量 vector

    # 创建向量：函数c()

    x<-c(1.31,1.46,2.23,4.113,5.323) # 创建数值向量

    y<-c(TRUE,FALSE,TRUE,TRUE)   # 创建逻辑性向量

    z<-c('a','ab','c','d')   # 创建字符型向量

    a_vector <- c(2:10)  # 连续数值序列向量

    ## 标量，只有一个元素的向量
    a<-8

    b<-'as'

    # 访问向量
    print(x)

    ## [1] 1.310 1.460 2.230 4.113 5.323

    x[2:4]  # 查看向量的第2到第4个元素

    ## [1] 1.460 2.230 4.113

    x[c(1,3)] # 访问向量的第1和第3个元素

    ## [1] 1.31 2.23

    # 判断是否为向量,返回逻辑型TRUE or FALSE
    is.vector(x)

    ## [1] TRUE

    # 计算向量长度（元素数量）
    length(x)

    ## [1] 5

向量的运算

    # 向量的运算:一一对应
    x1<-c(1,2,3,4,5,6,7,8,9)
    y1<-c(2,1,3,5,6,7,8,9,0)
    x1+y1

    ## [1]  3  3  6  9 11 13 15 17  9

    x1*y1

    ## [1]  2  2  9 20 30 42 56 72  0

### 2.2 矩阵 matrix

    # 创建矩阵，matrix()

    # 创建矩阵matrix(元素，行数，列数，按行（TRUE）按列（FALSE）填充，dimnames=list（行名，列名）)
    matrix1<-matrix(2:10,  # 创建矩阵的元素
                    nrow = 3,     # 矩阵行数
                    ncol = 3,     # 矩阵列数
                    byrow = TRUE,  # 元素是否按行填充
                    dimnames =list(c('A','B','C'),c('Q','E','R'))  # 行名和列名
                    )
    matrix1

    ##   Q E  R
    ## A 2 3  4
    ## B 5 6  7
    ## C 8 9 10

    # 访问矩阵内元素

    my_matrix<-matrix(factors<-c(1,2,1,3,2,4,3,9),nrow=2,ncol=4,byrow=TRUE,
                      dimnames=list(r_name<-c("R1","R2"),c_name<-c("C1","C2","C3","C4")))

    my_matrix[2,] # 访问矩阵的第二行元素

    ## C1 C2 C3 C4 
    ##  2  4  3  9

    my_matrix[,3] # 访问矩阵第三列元素

    ## R1 R2 
    ##  1  3

    my_matrix[2,3] # # 访问矩阵内第2行，第3列的元素，matrix[i,j]

    ## [1] 3

矩阵的计算

    # 矩阵乘法
    a<-matrix(2:6)  # 创建列矩阵（只有一列）
    b<-matrix(6:10,1) # 创建行矩阵（只有一行）

    c <- a%*%b # 内积
    c

    ##      [,1] [,2] [,3] [,4] [,5]
    ## [1,]   12   14   16   18   20
    ## [2,]   18   21   24   27   30
    ## [3,]   24   28   32   36   40
    ## [4,]   30   35   40   45   50
    ## [5,]   36   42   48   54   60

    d<-a%o%b # 外积
    d

    ## , , 1, 1
    ## 
    ##      [,1]
    ## [1,]   12
    ## [2,]   18
    ## [3,]   24
    ## [4,]   30
    ## [5,]   36
    ## 
    ## , , 1, 2
    ## 
    ##      [,1]
    ## [1,]   14
    ## [2,]   21
    ## [3,]   28
    ## [4,]   35
    ## [5,]   42
    ## 
    ## , , 1, 3
    ## 
    ##      [,1]
    ## [1,]   16
    ## [2,]   24
    ## [3,]   32
    ## [4,]   40
    ## [5,]   48
    ## 
    ## , , 1, 4
    ## 
    ##      [,1]
    ## [1,]   18
    ## [2,]   27
    ## [3,]   36
    ## [4,]   45
    ## [5,]   54
    ## 
    ## , , 1, 5
    ## 
    ##      [,1]
    ## [1,]   20
    ## [2,]   30
    ## [3,]   40
    ## [4,]   50
    ## [5,]   60

    # 矩阵的转置
    t(c)

    ##      [,1] [,2] [,3] [,4] [,5]
    ## [1,]   12   18   24   30   36
    ## [2,]   14   21   28   35   42
    ## [3,]   16   24   32   40   48
    ## [4,]   18   27   36   45   54
    ## [5,]   20   30   40   50   60

    # 矩阵的行列式
    det(c)

    ## [1] 0

### 2.3 数组 array

    # 用array()函数创建大于二维平面的数组，

    num<-c(1:25)
    dim1<- c("x1","x2")
    dim2<- c("y1","y2","y3")
    dim3<- c("z1","z2","z3","z4","z5")

    # 创建数组
    my_array<-array(num,    # 创建数组的元素
                    c(2,3,5),  # 各维度下标的最大值，即每个维度几行、几列、几层
                    dimnames=list(dim1,dim2,dim3)) # 各维度的标签，名称
    my_array

    ## , , z1
    ## 
    ##    y1 y2 y3
    ## x1  1  3  5
    ## x2  2  4  6
    ## 
    ## , , z2
    ## 
    ##    y1 y2 y3
    ## x1  7  9 11
    ## x2  8 10 12
    ## 
    ## , , z3
    ## 
    ##    y1 y2 y3
    ## x1 13 15 17
    ## x2 14 16 18
    ## 
    ## , , z4
    ## 
    ##    y1 y2 y3
    ## x1 19 21 23
    ## x2 20 22 24
    ## 
    ## , , z5
    ## 
    ##    y1 y2 y3
    ## x1 25  2  4
    ## x2  1  3  5

    my_array[1,2,3] # dim1中x1，dim2中y2，dim3中z3的元素

    ## [1] 15

### 2.4 数据框 dataframe

    # 创建数据框data.frame(,),每一列的数据是相同格式的
    num1<-c(1,2,3,4)
    name<-c("zero","one","two","three")
    num2<-c(2,3,4,5)

    # 创建数据框，每列的元素个数相同
    my_data<-data.frame(ID = num1, # ID为第一列的列明，num1为第一列的元素
                        name = name,
                        value = num2)
    my_data

    ##   ID  name value
    ## 1  1  zero     2
    ## 2  2   one     3
    ## 3  3   two     4
    ## 4  4 three     5

    #数据框访问（调用）
    my_data[1]  # 调用数据框第一列数据

    ##   ID
    ## 1  1
    ## 2  2
    ## 3  3
    ## 4  4

    my_data[c("ID")] # 通过列明调用ID列

    ##   ID
    ## 1  1
    ## 2  2
    ## 3  3
    ## 4  4

    my_data$name    # 表示从my_data数据框内访问name列

    ## [1] "zero"  "one"   "two"   "three"

    # 访问数据框
    my_data[,1:2] # 访问数据框的第一到第二列数据

    ##   ID  name
    ## 1  1  zero
    ## 2  2   one
    ## 3  3   two
    ## 4  4 three

    my_data[1:2,] # 访问数据框的第一、二行

    ##   ID name value
    ## 1  1 zero     2
    ## 2  2  one     3

    my_data[1:2,1:2] # 访问数据框的第一、二行的第一、二列的元素

    ##   ID name
    ## 1  1 zero
    ## 2  2  one

    # 显示数据框的信息，
    str(my_data) 

    ## 'data.frame':    4 obs. of  3 variables:
    ##  $ ID   : num  1 2 3 4
    ##  $ name : chr  "zero" "one" "two" "three"
    ##  $ value: num  2 3 4 5

    # 对数据框不同变量做不同处理，连续性的数值变量会求最值，均值，各四分位数，类别型变量显示频数等
    summary(my_data) 

    ##        ID           name               value     
    ##  Min.   :1.00   Length:4           Min.   :2.00  
    ##  1st Qu.:1.75   Class :character   1st Qu.:2.75  
    ##  Median :2.50   Mode  :character   Median :3.50  
    ##  Mean   :2.50                      Mean   :3.50  
    ##  3rd Qu.:3.25                      3rd Qu.:4.25  
    ##  Max.   :4.00                      Max.   :5.00

数据框从搜索路径添加、移除

    attach(my_data)# 将数据框添加到搜索路径

    ## The following object is masked _by_ .GlobalEnv:
    ## 
    ##     name

    detach(my_data) # 将数据框从搜索路径移除

### 2.5 因子 factor

    # 创建因子 factor(),类似分组变量

    diabetes <- c("type1","type2","type1","type1") # 表示名义形变量

    # 创建因子变量
    diabetes1 <- factor(diabetes) # 这里将diabetes<-c("type1","type2","type1","type1")存储为（1，2，1，1）向量，即存储为因子

    diabetes1

    ## [1] type1 type2 type1 type1
    ## Levels: type1 type2

    # 表示有序型变量
    status<-c("poor","improve","excellent","poor")
    status1<-factor(status,ordered = TRUE)
    status1 # 输出结果表明顺序为excellent < improve < poor，此时默认按字母排列顺序

    ## [1] poor      improve   excellent poor     
    ## Levels: excellent < improve < poor

    # 用levels=（）指定顺序
    status2<-factor(status,order=TRUE,
                    levels=c("poor","iaprove","excellent"))
    status2

    ## [1] poor      <NA>      excellent poor     
    ## Levels: poor < iaprove < excellent

    # 数值型变量用levels labels编码成因子
    sex <- c(1,2,2,2,1,1,1,2,2,2,1,1,2,1,2,1,1)
    sex_factor <- factor(sex,levels = c(1:2),labels=c('Male','Female'))

    sex

    ##  [1] 1 2 2 2 1 1 1 2 2 2 1 1 2 1 2 1 1

    sex_factor

    ##  [1] Male   Female Female Female Male   Male   Male   Female Female Female
    ## [11] Male   Male   Female Male   Female Male   Male  
    ## Levels: Male Female

### 2.6 列表 list

    # 创建列表list(),列表内可以是向量，矩阵，数据框，标量
    a<-c(1,2,3,4,5)
    b<-matrix(c(12,2,1,2,1,2,1,2,1,2,1,2),3,4)
    c<-data.frame(num1=c(1,2,3,4),
                  name=c("zero","one","two","three"),
                  num2=c(2,3,4,5))

    my_list<-list(a,b,c)
    my_list

    ## [[1]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[2]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[3]]
    ##   num1  name num2
    ## 1    1  zero    2
    ## 2    2   one    3
    ## 3    3   two    4
    ## 4    4 three    5

    # 访问列表内的内容
    my_list[3] # my_list[[3]]访问列表的第三部分，即这里的数据框

    ## [[1]]
    ##   num1  name num2
    ## 1    1  zero    2
    ## 2    2   one    3
    ## 3    3   two    4
    ## 4    4 three    5

    my_list[b]

    ## [[1]]
    ## NULL
    ## 
    ## [[2]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[3]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[4]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[5]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[6]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[7]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[8]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[9]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[10]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2
    ## 
    ## [[11]]
    ## [1] 1 2 3 4 5
    ## 
    ## [[12]]
    ##      [,1] [,2] [,3] [,4]
    ## [1,]   12    2    1    2
    ## [2,]    2    1    2    1
    ## [3,]    1    2    1    2

### 补充：R的基本语句

R的基本语句包括：条件语句、循环语句

条件语句：if语句、if···else语句、if··else if···语句

#### 条件语句

-   **if语句**

<!-- -->

    # if语句的基本结构

    # if( 条件判断语句 ){
    #   条件判断为TRUE是执行的命令
    # }

    # if语句的示例

    a <- 3
    if(a > 2){
      print('a is bigger than 2')
    }

    ## [1] "a is bigger than 2"

-   **if···else语句**

<!-- -->

    # if···else语句的基本结构

    # if( 条件判断语句 ){
    #   条件判断为TRUE是执行的命令
    # }else{
    #   条件语句判断为FAlSE时执行的命令
    # }


    # if···else语句示例

    b <- 5
    if( b*3 == 15){
      print('b is 5')
    }else{
      print('b is not 5')
    }

    ## [1] "b is 5"

-   **多个if···else嵌套的条件语句**

<!-- -->

    c <- 66

    if( c >5 ){
      print('c的值大于5')
    }else if(c == 5){
      print('c的值是5')
    }else{
      print('c的值小于5')
    }

    ## [1] "c的值大于5"

#### 循环语句

-   repeat循环

-   while循环

-   for循环

## 3、R导入数据

设置工作路径

    path = "A:/Rstudio/学习R/学习R_数据"

    setwd(path)

    dir() # 查看当前工作目录下的文件

    ##  [1] "~$merged_output.xlsx"   "data_823.csv"           "data_823.xlsx"         
    ##  [4] "GSM6422903.txt"         "merged_output.xlsx"     "RNA_seq _analysis.xlsx"
    ##  [7] "RNA_seq.xlsx"           "Rplot.tiff"             "significant_genes.csv" 
    ## [10] "第九批_AF.xlsx"         "工作簿2.xlsx"           "公司数据.xlsx"         
    ## [13] "江西油价.xlsx"          "油价.csv"

### 3.1、导入文本文件(\*\*\* .txt)

    # 读取文本文件txt，设置sep = ','
    data_txt <- read.table("A:/Rstudio/学习R/学习R_数据/GSM6422903.txt", # 文件路径
                           header = TRUE,  # 第一行是否为列名
                           sep = '\t')   # 读取制表符分隔行 的文件

### 3.2、导入Excel文件（\*\*\*.xlsx)

    # 用readxl包读取
    library(readxl)
    data_excel <- read_excel("A:/Rstudio/学习R/学习R_数据/江西油价.xlsx",  # 文件路径
                             sheet = 1)         # 按excel的shell索引

    # 其他包，openxl安装需要先安装Rtools

### 3.3、导入csv文件（\*\*\*.csv)

    data_csv <- read.csv("A:/Rstudio/学习R/学习R_数据/油价.csv",
                         fileEncoding = "GB18030") # 有中文时，传此参数

## 4、R统计分析

### 4.1、描述统计

#### 4.1.1、了解数据的分布情况、集中趋势和离散程度等信息

    # 以iris数据集为例，介绍R对数据进行描述统计
    data <- iris # 读取iris数据集
    head(data,10) # 查看iris数据的前10行

    ##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1           5.1         3.5          1.4         0.2  setosa
    ## 2           4.9         3.0          1.4         0.2  setosa
    ## 3           4.7         3.2          1.3         0.2  setosa
    ## 4           4.6         3.1          1.5         0.2  setosa
    ## 5           5.0         3.6          1.4         0.2  setosa
    ## 6           5.4         3.9          1.7         0.4  setosa
    ## 7           4.6         3.4          1.4         0.3  setosa
    ## 8           5.0         3.4          1.5         0.2  setosa
    ## 9           4.4         2.9          1.4         0.2  setosa
    ## 10          4.9         3.1          1.5         0.1  setosa

    # 计算iris数据集的sepal.length的情况

    # 反映数据的集中情况
    mean(iris$Sepal.Length)  # 均值，反映集中情况

    ## [1] 5.843333

    median(iris$Sepal.Length)  # 中位数，反映集中情况

    ## [1] 5.8

    mode(iris$Sepal.Length)  # 众数，反映集中情况

    ## [1] "numeric"

    # 反映数据的分散情况
    max(iris$Sepal.Length)  # 最大值，

    ## [1] 7.9

    min(iris$Sepal.Length)  # 最小值

    ## [1] 4.3

    range(iris$Sepal.Length) # 输出极差

    ## [1] 4.3 7.9

    var(iris$Sepal.Length)  # 方差

    ## [1] 0.6856935

    sd(iris$Sepal.Length)  # 标准差

    ## [1] 0.8280661

    # 一个函数解决描述统计
    summary(iris$Sepal.Length)  

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   4.300   5.100   5.800   5.843   6.400   7.900

#### 4.1.2、数据的分布形态

通过图反映数据分布形态，分布形态包括：偏态+峰度

偏态

除了集中趋势和离散趋势,我们还需要了解数据的分布形态。常见的分布形态有偏态和峰度。

偏态描述数据分布的对称性,分为左偏(负偏)、对称和右偏(正偏)三种情况。

偏度系数的取值范围为(-∞,+∞),0
表示数据分布对称,负值表示左偏,正值表示右偏。

通过观察数据的**直方图**或计算**偏度系数**来判断数据的**偏态**。

    library(moments)

    # 绘制直方图
    hist(iris$Sepal.Length) # 绘制直方图

![](学习R_files/figure-markdown_strict/unnamed-chunk-26-1.png)

    skewness(iris$Sepal.Length)  # 计算偏度系数，右偏

    ## [1] 0.3117531

    hist(iris$Sepal.Width)  # 绘制直方图

![](学习R_files/figure-markdown_strict/unnamed-chunk-26-2.png)

    skewness(iris$Sepal.Width)  # 计算偏度系数,右偏

    ## [1] 0.3157671

峰度

峰度描述数据分布曲线顶部的尖峭或平坦程度,分为尖顶(leptokurtic)、正态(mesokurtic)和平顶(platykurtic)三种情况。

我们可以通过观察数据的 QQ 图或计算峰度系数来判断数据的峰度。QQ
图可以用来检验数据是否符合正态分布。如果数据点大致落在参考线上,则数据可能服从正态分布。

在 R 中,可以使用 qqnorm()函数绘制 QQ 图,moments 包的
kurtosis()函数计算峰度系数。峰度系数的取值范围为(-∞,+∞),0
表示数据符合正态分布,大于 0 为尖顶,小于 0 为平顶。

    # 计算峰度
    library(moments)
    kurtosis(iris$Sepal.Length)

    ## [1] 2.426432

    # 绘制QQ图
    qqnorm(iris$Sepal.Length)
    qqline(iris$Sepal.Width)

![](学习R_files/figure-markdown_strict/unnamed-chunk-27-1.png)

## 4.2、假设检验

假设检验是统计推断的重要方法,用于根据样本数据对总体参数或分布做出推断。它的基本思想是,先对总体提出一个假设(原假设),然后通过样本数据来验证这个假设是否成立。如果样本数据与原假设出现较大差异,我们就有理由拒绝原假设。

### 4.2.1、T检验

**T检验**（T-test） 是一种统计假设检验方法，用于判断两组数据的**均值**是否存在显著差异。它的核心思想是通过比较样本均值的差异与数据变异性（标准差）的关系，推断这种差异是否具有统计学意义。

**T检验的适用条件**

1.  **数据类型**：连续变量（如身高、温度、考试成绩等）。

2.  **分布要求**：

    -   数据应近似服从正态分布（尤其是小样本时，n &lt; 30）。

    -   若样本量较大（n ≥ 30），根据中心极限定理，可放宽正态性要求。

3.  **方差齐性**：两独立样本T检验要求两组数据的方差大致相等（可通过Levene检验或F检验判断）。

T检验包括：单样本T检验、独立样本T检验、配对样本T检验

#### 单样本T检验（One-Sample T-test）

-   **目的**：检验单个样本的均值是否与已知的总体均值存在显著差异。

-   公式：其中Xˉ为样本均值，μ为总体均值，s为样本标准差，n为样本量。

<!-- -->

    ![](images/clipboard-38014.png)

    # 假设样本
    a_sample <- c(2,3,4,2,1,4,2,3,4,5,2,3,2,1,4,5,3,2,1,2,3,4,4)

    # 假设总体均值为2.5
    means <- 2.5

    t.test(a_sample,mu = means)

    ## 
    ##  One Sample t-test
    ## 
    ## data:  a_sample
    ## t = 1.4558, df = 22, p-value = 0.1596
    ## alternative hypothesis: true mean is not equal to 2.5
    ## 95 percent confidence interval:
    ##  2.343095 3.396035
    ## sample estimates:
    ## mean of x 
    ##  2.869565

    # 小样本，正态性假设检验
    shapiro.test(a_sample) # Shapiro-Wilk检验（p > 0.05时认为正态）

    ## 
    ##  Shapiro-Wilk normality test
    ## 
    ## data:  a_sample
    ## W = 0.91509, p-value = 0.05235

    # 上述正态性检验表示，不符合正态性，误差大，选择用非参数检验
    # 非参数检验的Wilcoxon符号秩检验
    wilcox.test(a_sample, mu = means)

    ## Warning in wilcox.test.default(a_sample, mu = means): cannot compute exact
    ## p-value with ties

    ## 
    ##  Wilcoxon signed rank test with continuity correction
    ## 
    ## data:  a_sample
    ## V = 179.5, p-value = 0.2014
    ## alternative hypothesis: true location is not equal to 2.5

    # 用箱图对结果进行可视化
    boxplot(a_sample,main = '单样本T检验')
    abline(h = means,col = 'red',lty = 2) # 添加理论均值参考线

![](学习R_files/figure-markdown_strict/unnamed-chunk-28-1.png)

#### 独立样本T检验

**独立样本t检验**（Independent Samples
t-test）用于比较**两组独立数据**的均值是否存在显著差异。

步骤：检查两组数据是否是连续型——检查两组数据是否服从正态分布——检查数据两组数据是否方差齐性——T检验——结果可视化

**对于非正态数据**：考虑使用非参数检验（如Mann-Whitney
U检验，**`wilcox.test(value ~ group, data = data)`**）。

    # 以iris的两列数据比较作为示例
    head(iris)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    # 根据一列分组变量提取对应列的数据和组数据，这里我们根据Species的分组变量，对setosa和versicolor两组及其对应的Sepal.Length数据提取出来
    iris_T <- subset(iris, Species %in% c("setosa", "versicolor"), 
                          select = c("Sepal.Length", "Species"))

    # 比较sepal.length在setosa和versicolor两个品种间是否有差异

    # 用Shapiro-Wilk检验或QQ图对两组数据的正太性进行检验,p>0.05,认为服从正太分布

    shapiro_setosa <- shapiro.test(iris_T$Sepal.Length[iris_T$Species=='setosa'])  # 
    shapiro_versicolor <- shapiro.test(iris_T$Sepal.Length[iris_T$Species=='versicolor'])  # 
    print(c(shapiro_setosa,shapiro_versicolor))

    ## $statistic
    ##         W 
    ## 0.9776985 
    ## 
    ## $p.value
    ## [1] 0.4595132
    ## 
    ## $method
    ## [1] "Shapiro-Wilk normality test"
    ## 
    ## $data.name
    ## [1] "iris_T$Sepal.Length[iris_T$Species == \"setosa\"]"
    ## 
    ## $statistic
    ##         W 
    ## 0.9778357 
    ## 
    ## $p.value
    ## [1] 0.464737
    ## 
    ## $method
    ## [1] "Shapiro-Wilk normality test"
    ## 
    ## $data.name
    ## [1] "iris_T$Sepal.Length[iris_T$Species == \"versicolor\"]"

    # 方差齐性检验,P>0.05认为方差齐性
    library(car)

    ## Loading required package: carData

    leveneTest(iris_T$Sepal.Length,iris_T$Species,data = iris)

    ## Levene's Test for Homogeneity of Variance (center = median: iris)
    ##       Df F value   Pr(>F)   
    ## group  1  8.1727 0.005196 **
    ##       98                    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    # 执行t检验
    # 若方差齐性（var.equal = TRUE）：使用Student's t-test。
    # 若方差不齐（var.equal = FALSE）：使用Welch's t-test（默认）

    t.test(iris_T$Sepal.Length[iris_T$Species=='setosa'],
           iris$Sepal.Length[iris$Species=='versicolor'],var.equal = T)  # 方差齐性

    ## 
    ##  Two Sample t-test
    ## 
    ## data:  iris_T$Sepal.Length[iris_T$Species == "setosa"] and iris$Sepal.Length[iris$Species == "versicolor"]
    ## t = -10.521, df = 98, p-value < 2.2e-16
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##  -1.1054165 -0.7545835
    ## sample estimates:
    ## mean of x mean of y 
    ##     5.006     5.936

    t.test(iris_T$Sepal.Length[iris_T$Species=='setosa'],
           iris_T$Sepal.Length[iris_T$Species=='versicolor'],var.equal = F)  # 方差不齐性

    ## 
    ##  Welch Two Sample t-test
    ## 
    ## data:  iris_T$Sepal.Length[iris_T$Species == "setosa"] and iris_T$Sepal.Length[iris_T$Species == "versicolor"]
    ## t = -10.521, df = 86.538, p-value < 2.2e-16
    ## alternative hypothesis: true difference in means is not equal to 0
    ## 95 percent confidence interval:
    ##  -1.1057074 -0.7542926
    ## sample estimates:
    ## mean of x mean of y 
    ##     5.006     5.936

    # 结果可视化
    library(ggplot2)
    library(ggpubr)  # 用于添加统计标记

    ggplot(iris_T, aes(x = Species, y = Sepal.Length, fill = Species)) +
      geom_boxplot(alpha = 0.7) +
      geom_jitter(width = 0.1, alpha = 0.5) +  # 显示数据点
      stat_compare_means(method = "t.test", label = "p.format") +  # 添加p值
      labs(title = "T-Test", x = "Species", y = "sepal.Length") +
      theme_minimal()

![](学习R_files/figure-markdown_strict/unnamed-chunk-29-1.png)

#### 配对样本T检验

用于比较**同一组受试对象**在两种不同条件下的测量值是否存在显著差异（如治疗前后、两种方法的测量结果等）

**实际数据格式要求：**

-   两列数值变量（必须长度相同）。

-   每行代表同一受试对象的配对测量。

**检查配对t检验的假设**

配对t检验需满足：

1.  **配对性**：数据必须是同一组对象的两次测量。

2.  **差值正态性**：两列数据的差值近似服从正态分布（可用Shapiro-Wilk检验或QQ图检验）。

对于不服从正态分布的数据，改用**Wilcoxon符号秩检验**（非参数替代）wilcox.test(paired\_data*c**o**n**d**i**t**i**o**n*<sub>*A*</sub>, *p**a**i**r**e**d*<sub>*d*</sub>*a**t**a*condition\_B,
paired = TRUE)

    # 创建配对数据

    paired_data <- data.frame(
      flower_id = 1:50,  # 50朵setosa花
      condition_A = iris$Sepal.Length[iris$Species == "setosa"],  # 条件A的测量值
      condition_B = iris$Sepal.Length[iris$Species == "setosa"] + rnorm(50, mean = 0.5, sd = 0.3)  # 条件B的测量值（人为添加差异）
    )

    # 查看前6行
    head(paired_data)

    ##   flower_id condition_A condition_B
    ## 1         1         5.1    5.279346
    ## 2         2         4.9    6.050165
    ## 3         3         4.7    5.373334
    ## 4         4         4.6    5.119173
    ## 5         5         5.0    5.298185
    ## 6         6         5.4    5.626508

    #  检查差值正态性

    # 计算差值
    differences <- paired_data$condition_B - paired_data$condition_A

    # Shapiro-Wilk检验
    shapiro_test <- shapiro.test(differences)
    print(shapiro_test)  # p值 > 0.05说明差值服从正态分布

    ## 
    ##  Shapiro-Wilk normality test
    ## 
    ## data:  differences
    ## W = 0.98751, p-value = 0.8716

    # QQ图可视化
    qqnorm(differences)
    qqline(differences, col = "red")

![](学习R_files/figure-markdown_strict/unnamed-chunk-30-1.png)

    # 执行配对T检验
    t_test_result <- t.test(
      paired_data$condition_A, 
      paired_data$condition_B, 
      paired = TRUE,  # 关键参数，对于配对T检验，指定为T
      alternative = "two.sided"  # 双侧检验（默认）
    )

    print(t_test_result)

    ## 
    ##  Paired t-test
    ## 
    ## data:  paired_data$condition_A and paired_data$condition_B
    ## t = -9.6438, df = 49, p-value = 6.617e-13
    ## alternative hypothesis: true mean difference is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.5361039 -0.3512061
    ## sample estimates:
    ## mean difference 
    ##       -0.443655

    # 结果可视化
    # 方法1：箱线图 + 配对线（适合少量数据点）
    library(ggplot2)
    library(tidyr)

    # 转换数据为长格式
    paired_long <- pivot_longer(
      paired_data, 
      cols = c("condition_A", "condition_B"), 
      names_to = "condition", 
      values_to = "sepal_length"
    )

    # 绘制箱线图 + 配对线
    ggplot(paired_long, aes(x = condition, y = sepal_length)) +
      geom_boxplot(width = 0.5, fill = "lightblue") +
      geom_line(aes(group = flower_id), color = "gray", alpha = 0.5) +  # 配对线
      geom_point(aes(color = condition), size = 2) +
      labs(title = "Paired Samples t-test", x = "Condition", y = "Sepal Length") +
      theme_minimal()

![](学习R_files/figure-markdown_strict/unnamed-chunk-30-2.png)

    # 方法2：差异分布直方图
    ggplot(data.frame(differences), aes(x = differences)) +
      geom_histogram(binwidth = 0.1, fill = "skyblue", color = "black") +
      geom_vline(xintercept = mean(differences), color = "red", linetype = "dashed") +
      labs(title = "Distribution of Differences", x = "Difference (B - A)", y = "Frequency") +
      theme_minimal()

![](学习R_files/figure-markdown_strict/unnamed-chunk-30-3.png)

### 4.2.2、方差分析

方差分析(ANOVA)用于比较三个及以上样本均值的差异。根据因素的个数,方差分析可分为单因素方差分析和多因素方差分析。

#### 单因素方差分析

**检验方差齐性：**使用 **Levene检验**（对非正态数据更稳健）或 **Bartlett检验**（需数据正态）

**执行ANOVA**

**事后检验（多重比较）**

    # 以iris数据为例，比较不同Species（setosa, versicolor, virginica）的 Sepal.Length 均值差异。

    iris

    ##     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
    ## 1            5.1         3.5          1.4         0.2     setosa
    ## 2            4.9         3.0          1.4         0.2     setosa
    ## 3            4.7         3.2          1.3         0.2     setosa
    ## 4            4.6         3.1          1.5         0.2     setosa
    ## 5            5.0         3.6          1.4         0.2     setosa
    ## 6            5.4         3.9          1.7         0.4     setosa
    ## 7            4.6         3.4          1.4         0.3     setosa
    ## 8            5.0         3.4          1.5         0.2     setosa
    ## 9            4.4         2.9          1.4         0.2     setosa
    ## 10           4.9         3.1          1.5         0.1     setosa
    ## 11           5.4         3.7          1.5         0.2     setosa
    ## 12           4.8         3.4          1.6         0.2     setosa
    ## 13           4.8         3.0          1.4         0.1     setosa
    ## 14           4.3         3.0          1.1         0.1     setosa
    ## 15           5.8         4.0          1.2         0.2     setosa
    ## 16           5.7         4.4          1.5         0.4     setosa
    ## 17           5.4         3.9          1.3         0.4     setosa
    ## 18           5.1         3.5          1.4         0.3     setosa
    ## 19           5.7         3.8          1.7         0.3     setosa
    ## 20           5.1         3.8          1.5         0.3     setosa
    ## 21           5.4         3.4          1.7         0.2     setosa
    ## 22           5.1         3.7          1.5         0.4     setosa
    ## 23           4.6         3.6          1.0         0.2     setosa
    ## 24           5.1         3.3          1.7         0.5     setosa
    ## 25           4.8         3.4          1.9         0.2     setosa
    ## 26           5.0         3.0          1.6         0.2     setosa
    ## 27           5.0         3.4          1.6         0.4     setosa
    ## 28           5.2         3.5          1.5         0.2     setosa
    ## 29           5.2         3.4          1.4         0.2     setosa
    ## 30           4.7         3.2          1.6         0.2     setosa
    ## 31           4.8         3.1          1.6         0.2     setosa
    ## 32           5.4         3.4          1.5         0.4     setosa
    ## 33           5.2         4.1          1.5         0.1     setosa
    ## 34           5.5         4.2          1.4         0.2     setosa
    ## 35           4.9         3.1          1.5         0.2     setosa
    ## 36           5.0         3.2          1.2         0.2     setosa
    ## 37           5.5         3.5          1.3         0.2     setosa
    ## 38           4.9         3.6          1.4         0.1     setosa
    ## 39           4.4         3.0          1.3         0.2     setosa
    ## 40           5.1         3.4          1.5         0.2     setosa
    ## 41           5.0         3.5          1.3         0.3     setosa
    ## 42           4.5         2.3          1.3         0.3     setosa
    ## 43           4.4         3.2          1.3         0.2     setosa
    ## 44           5.0         3.5          1.6         0.6     setosa
    ## 45           5.1         3.8          1.9         0.4     setosa
    ## 46           4.8         3.0          1.4         0.3     setosa
    ## 47           5.1         3.8          1.6         0.2     setosa
    ## 48           4.6         3.2          1.4         0.2     setosa
    ## 49           5.3         3.7          1.5         0.2     setosa
    ## 50           5.0         3.3          1.4         0.2     setosa
    ## 51           7.0         3.2          4.7         1.4 versicolor
    ## 52           6.4         3.2          4.5         1.5 versicolor
    ## 53           6.9         3.1          4.9         1.5 versicolor
    ## 54           5.5         2.3          4.0         1.3 versicolor
    ## 55           6.5         2.8          4.6         1.5 versicolor
    ## 56           5.7         2.8          4.5         1.3 versicolor
    ## 57           6.3         3.3          4.7         1.6 versicolor
    ## 58           4.9         2.4          3.3         1.0 versicolor
    ## 59           6.6         2.9          4.6         1.3 versicolor
    ## 60           5.2         2.7          3.9         1.4 versicolor
    ## 61           5.0         2.0          3.5         1.0 versicolor
    ## 62           5.9         3.0          4.2         1.5 versicolor
    ## 63           6.0         2.2          4.0         1.0 versicolor
    ## 64           6.1         2.9          4.7         1.4 versicolor
    ## 65           5.6         2.9          3.6         1.3 versicolor
    ## 66           6.7         3.1          4.4         1.4 versicolor
    ## 67           5.6         3.0          4.5         1.5 versicolor
    ## 68           5.8         2.7          4.1         1.0 versicolor
    ## 69           6.2         2.2          4.5         1.5 versicolor
    ## 70           5.6         2.5          3.9         1.1 versicolor
    ## 71           5.9         3.2          4.8         1.8 versicolor
    ## 72           6.1         2.8          4.0         1.3 versicolor
    ## 73           6.3         2.5          4.9         1.5 versicolor
    ## 74           6.1         2.8          4.7         1.2 versicolor
    ## 75           6.4         2.9          4.3         1.3 versicolor
    ## 76           6.6         3.0          4.4         1.4 versicolor
    ## 77           6.8         2.8          4.8         1.4 versicolor
    ## 78           6.7         3.0          5.0         1.7 versicolor
    ## 79           6.0         2.9          4.5         1.5 versicolor
    ## 80           5.7         2.6          3.5         1.0 versicolor
    ## 81           5.5         2.4          3.8         1.1 versicolor
    ## 82           5.5         2.4          3.7         1.0 versicolor
    ## 83           5.8         2.7          3.9         1.2 versicolor
    ## 84           6.0         2.7          5.1         1.6 versicolor
    ## 85           5.4         3.0          4.5         1.5 versicolor
    ## 86           6.0         3.4          4.5         1.6 versicolor
    ## 87           6.7         3.1          4.7         1.5 versicolor
    ## 88           6.3         2.3          4.4         1.3 versicolor
    ## 89           5.6         3.0          4.1         1.3 versicolor
    ## 90           5.5         2.5          4.0         1.3 versicolor
    ## 91           5.5         2.6          4.4         1.2 versicolor
    ## 92           6.1         3.0          4.6         1.4 versicolor
    ## 93           5.8         2.6          4.0         1.2 versicolor
    ## 94           5.0         2.3          3.3         1.0 versicolor
    ## 95           5.6         2.7          4.2         1.3 versicolor
    ## 96           5.7         3.0          4.2         1.2 versicolor
    ## 97           5.7         2.9          4.2         1.3 versicolor
    ## 98           6.2         2.9          4.3         1.3 versicolor
    ## 99           5.1         2.5          3.0         1.1 versicolor
    ## 100          5.7         2.8          4.1         1.3 versicolor
    ## 101          6.3         3.3          6.0         2.5  virginica
    ## 102          5.8         2.7          5.1         1.9  virginica
    ## 103          7.1         3.0          5.9         2.1  virginica
    ## 104          6.3         2.9          5.6         1.8  virginica
    ## 105          6.5         3.0          5.8         2.2  virginica
    ## 106          7.6         3.0          6.6         2.1  virginica
    ## 107          4.9         2.5          4.5         1.7  virginica
    ## 108          7.3         2.9          6.3         1.8  virginica
    ## 109          6.7         2.5          5.8         1.8  virginica
    ## 110          7.2         3.6          6.1         2.5  virginica
    ## 111          6.5         3.2          5.1         2.0  virginica
    ## 112          6.4         2.7          5.3         1.9  virginica
    ## 113          6.8         3.0          5.5         2.1  virginica
    ## 114          5.7         2.5          5.0         2.0  virginica
    ## 115          5.8         2.8          5.1         2.4  virginica
    ## 116          6.4         3.2          5.3         2.3  virginica
    ## 117          6.5         3.0          5.5         1.8  virginica
    ## 118          7.7         3.8          6.7         2.2  virginica
    ## 119          7.7         2.6          6.9         2.3  virginica
    ## 120          6.0         2.2          5.0         1.5  virginica
    ## 121          6.9         3.2          5.7         2.3  virginica
    ## 122          5.6         2.8          4.9         2.0  virginica
    ## 123          7.7         2.8          6.7         2.0  virginica
    ## 124          6.3         2.7          4.9         1.8  virginica
    ## 125          6.7         3.3          5.7         2.1  virginica
    ## 126          7.2         3.2          6.0         1.8  virginica
    ## 127          6.2         2.8          4.8         1.8  virginica
    ## 128          6.1         3.0          4.9         1.8  virginica
    ## 129          6.4         2.8          5.6         2.1  virginica
    ## 130          7.2         3.0          5.8         1.6  virginica
    ## 131          7.4         2.8          6.1         1.9  virginica
    ## 132          7.9         3.8          6.4         2.0  virginica
    ## 133          6.4         2.8          5.6         2.2  virginica
    ## 134          6.3         2.8          5.1         1.5  virginica
    ## 135          6.1         2.6          5.6         1.4  virginica
    ## 136          7.7         3.0          6.1         2.3  virginica
    ## 137          6.3         3.4          5.6         2.4  virginica
    ## 138          6.4         3.1          5.5         1.8  virginica
    ## 139          6.0         3.0          4.8         1.8  virginica
    ## 140          6.9         3.1          5.4         2.1  virginica
    ## 141          6.7         3.1          5.6         2.4  virginica
    ## 142          6.9         3.1          5.1         2.3  virginica
    ## 143          5.8         2.7          5.1         1.9  virginica
    ## 144          6.8         3.2          5.9         2.3  virginica
    ## 145          6.7         3.3          5.7         2.5  virginica
    ## 146          6.7         3.0          5.2         2.3  virginica
    ## 147          6.3         2.5          5.0         1.9  virginica
    ## 148          6.5         3.0          5.2         2.0  virginica
    ## 149          6.2         3.4          5.4         2.3  virginica
    ## 150          5.9         3.0          5.1         1.8  virginica

    head(iris)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    # 方差齐性检验, Levene检验（对非正态数据更稳健）或Bartlett检验（需数据正态）：
    library(car)

    leveneTest(Sepal.Length ~ Species, data = iris) # p > 0.05说明方差齐性

    ## Levene's Test for Homogeneity of Variance (center = median)
    ##        Df F value   Pr(>F)   
    ## group   2  6.3527 0.002259 **
    ##       147                    
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    bartlett.test(Sepal.Length ~ Species, data = iris) 

    ## 
    ##  Bartlett test of homogeneity of variances
    ## 
    ## data:  Sepal.Length by Species
    ## Bartlett's K-squared = 16.006, df = 2, p-value = 0.0003345

    # 执行方差分析（ANOVA)
    anova_result <- aov(Sepal.Length ~ Species, data = iris)
    summary(anova_result)

    ##              Df Sum Sq Mean Sq F value Pr(>F)    
    ## Species       2  63.21  31.606   119.3 <2e-16 ***
    ## Residuals   147  38.96   0.265                   
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    # 事后检验（多重比较）
    TukeyHSD(anova_result)  # 输出各组间的p值和差异

    ##   Tukey multiple comparisons of means
    ##     95% family-wise confidence level
    ## 
    ## Fit: aov(formula = Sepal.Length ~ Species, data = iris)
    ## 
    ## $Species
    ##                       diff       lwr       upr p adj
    ## versicolor-setosa    0.930 0.6862273 1.1737727     0
    ## virginica-setosa     1.582 1.3382273 1.8257727     0
    ## virginica-versicolor 0.652 0.4082273 0.8957727     0

    plot(TukeyHSD(anova_result))  # 可视化置信区间

![](学习R_files/figure-markdown_strict/unnamed-chunk-31-1.png)

    # 统计分析结果的可视化
    # 箱线图 + 显著性标记（ggplot2 + ggpubr）
    library(ggplot2)
    library(ggpubr)

    ggplot(iris, aes(x = Species, y = Sepal.Length, fill = Species)) +
      geom_boxplot() +
      stat_compare_means(method = "anova", label.y = 9.5) +  # 添加ANOVA p值
      stat_compare_means(comparisons = list(c("setosa", "versicolor"), 
                         c("versicolor", "virginica"),c('setosa','virginica')), 
                       method = "t.test", label = "p.signif") +  # 组间比较
      labs(title = "One-Way ANOVA: Sepal Length by Species")

![](学习R_files/figure-markdown_strict/unnamed-chunk-31-2.png)

(
**非参数替代（当数据不满足ANOVA假设）:**若数据不满足正态性或方差齐性，使用
**Kruskal-Wallis检验**（单因素）或 **Friedman检验**（重复测量）)

    # 单因素非参数检验
    kruskal.test(Sepal.Length ~ Species, data = iris)

    ## 
    ##  Kruskal-Wallis rank sum test
    ## 
    ## data:  Sepal.Length by Species
    ## Kruskal-Wallis chi-squared = 96.937, df = 2, p-value < 2.2e-16

    # 事后比较（Dunn检验）
    library(FSA)

    ## Registered S3 methods overwritten by 'FSA':
    ##   method       from
    ##   confint.boot car 
    ##   hist.boot    car

    ## ## FSA v0.10.0. See citation('FSA') if used in publication.
    ## ## Run fishR() for related website and fishR('IFAR') for related book.

    ## 
    ## Attaching package: 'FSA'

    ## The following object is masked from 'package:car':
    ## 
    ##     bootCase

    dunnTest(Sepal.Length ~ Species, data = iris, method = "bonferroni")

    ## Dunn (1964) Kruskal-Wallis multiple comparison

    ##   p-values adjusted with the Bonferroni method.

    ##               Comparison         Z      P.unadj        P.adj
    ## 1    setosa - versicolor -6.106326 1.019504e-09 3.058513e-09
    ## 2     setosa - virginica -9.741785 2.000099e-22 6.000296e-22
    ## 3 versicolor - virginica -3.635459 2.774866e-04 8.324597e-04

#### **双因素方差分析（Two-Way ANOVA）**

以 **`ToothGrowth`** 数据集为例，分析牙齿长度（**`len`**）受 **剂量（`dose`）** 和 **补充剂类型（`supp`）** 的影响

    # 数据准备：
    data(ToothGrowth)
    ToothGrowth$dose <- factor(ToothGrowth$dose)  # 将剂量转为因子
    head(ToothGrowth)

    ##    len supp dose
    ## 1  4.2   VC  0.5
    ## 2 11.5   VC  0.5
    ## 3  7.3   VC  0.5
    ## 4  5.8   VC  0.5
    ## 5  6.4   VC  0.5
    ## 6 10.0   VC  0.5

    # 执行双因素ANOVA（含交互作用）：supp:dose：交互作用项（p < 0.05表示两者对结果有协同影响）。
    anova_two_way <- aov(len ~ supp * dose, data = ToothGrowth)
    summary(anova_two_way)

    ##             Df Sum Sq Mean Sq F value   Pr(>F)    
    ## supp         1  205.4   205.4  15.572 0.000231 ***
    ## dose         2 2426.4  1213.2  92.000  < 2e-16 ***
    ## supp:dose    2  108.3    54.2   4.107 0.021860 *  
    ## Residuals   54  712.1    13.2                     
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    library(emmeans)

    ## Welcome to emmeans.
    ## Caution: You lose important information if you filter this package's results.
    ## See '? untidy'

    emm <- emmeans(anova_two_way, pairwise ~ supp | dose)  # 按剂量分组比较supp
    plot(emm, comparisons = TRUE)  # 可视化

![](学习R_files/figure-markdown_strict/unnamed-chunk-33-1.png)

    # 交互作用图（双因素ANOVA）：
    ggplot(ToothGrowth, aes(x = dose, y = len, color = supp, group = supp)) +
      geom_point() +
      stat_summary(fun = mean, geom = "line") +  # 绘制均值连线
      labs(title = "Interaction Plot: Dose vs. Supplement Type")

![](学习R_files/figure-markdown_strict/unnamed-chunk-33-2.png)

### 4.2.3、卡方检验

主要用于分析**分类变量**之间的关联性或拟合优度,包括卡方独立性检验、卡方拟合优度检验

卡方独立性检验：检验两个分类变量是否独立（即是否存在关联）。

-   性别（男/女）与吸烟习惯（是/否）是否有关联？

-   广告类型（A/B/C）与购买意愿（高/中/低）是否相关？

<!-- -->

    # 以Titanic数据集为例，分析乘客等级（Class）与生存状态（Survived）是否独立。

    # 提取数据并转换为二维列联表
    Titanic # 查看数据集

    ## , , Age = Child, Survived = No
    ## 
    ##       Sex
    ## Class  Male Female
    ##   1st     0      0
    ##   2nd     0      0
    ##   3rd    35     17
    ##   Crew    0      0
    ## 
    ## , , Age = Adult, Survived = No
    ## 
    ##       Sex
    ## Class  Male Female
    ##   1st   118      4
    ##   2nd   154     13
    ##   3rd   387     89
    ##   Crew  670      3
    ## 
    ## , , Age = Child, Survived = Yes
    ## 
    ##       Sex
    ## Class  Male Female
    ##   1st     5      1
    ##   2nd    11     13
    ##   3rd    13     14
    ##   Crew    0      0
    ## 
    ## , , Age = Adult, Survived = Yes
    ## 
    ##       Sex
    ## Class  Male Female
    ##   1st    57    140
    ##   2nd    14     80
    ##   3rd    75     76
    ##   Crew  192     20

    data <- as.data.frame(Titanic)  # 将数据集转化为数据框
    head(data)

    ##   Class    Sex   Age Survived Freq
    ## 1   1st   Male Child       No    0
    ## 2   2nd   Male Child       No    0
    ## 3   3rd   Male Child       No   35
    ## 4  Crew   Male Child       No    0
    ## 5   1st Female Child       No    0
    ## 6   2nd Female Child       No    0

    titanic_table <- xtabs(Freq ~ Class + Survived, data = data)  # 创建二维列联表
    print(titanic_table)

    ##       Survived
    ## Class   No Yes
    ##   1st  122 203
    ##   2nd  167 118
    ##   3rd  528 178
    ##   Crew 673 212

    # 进行卡方检验
    # X-squared：卡方统计量。
    # df：自由度（(行数-1)*(列数-1)）。
    # p-value：显著性（p < 0.05 表示变量显著相关）。

    chi_test <- chisq.test(titanic_table)
    print(chi_test)

    ## 
    ##  Pearson's Chi-squared test
    ## 
    ## data:  titanic_table
    ## X-squared = 190.4, df = 3, p-value < 2.2e-16

    chi_test$expected  # 期望频数

    ##       Survived
    ## Class        No       Yes
    ##   1st  220.0136 104.98637
    ##   2nd  192.9350  92.06497
    ##   3rd  477.9373 228.06270
    ##   Crew 599.1140 285.88596

    chi_test$residuals # Pearson残差（标准化残差）

    ##       Survived
    ## Class         No       Yes
    ##   1st  -6.607873  9.565772
    ##   2nd  -1.867159  2.702959
    ##   3rd   2.289965 -3.315027
    ##   Crew  3.018611 -4.369840

    # 结果可视化，颜色越深，观测值与期望值的偏差越大。
    library(vcd)

    ## Loading required package: grid

    mosaic(titanic_table, shade = TRUE, legend = TRUE)

![](学习R_files/figure-markdown_strict/unnamed-chunk-34-1.png)

    a = 2
    switch(a,b = mean(a),a = a+3)

    ## [1] 5

### 4.2.4、相关性检验

相关性检验用于分析两个连续变量之间的线性关系（如身高与体重、广告投入与销售额

**效应量解读**

-   **|r| &lt; 0.3**：弱相关。

-   **0.3 ≤ |r| &lt; 0.7**：中等相关。

-   **|r| ≥ 0.7**：强相关。

<!-- -->

    # 以R内置数据集 mtcars 为例，分析 mpg（每加仑英里数）和 wt（车重）的相关性。

    data(mtcars)
    head(mtcars[, c("mpg", "wt")])

    ##                    mpg    wt
    ## Mazda RX4         21.0 2.620
    ## Mazda RX4 Wag     21.0 2.875
    ## Datsun 710        22.8 2.320
    ## Hornet 4 Drive    21.4 3.215
    ## Hornet Sportabout 18.7 3.440
    ## Valiant           18.1 3.460

    # Pearson相关系数（线性相关）：数据满足正态性和线性关系

    # 计算Pearson相关系数
    cor_pearson <- cor.test(mtcars$mpg, mtcars$wt, method = "pearson")
    print(cor_pearson)

    ## 
    ##  Pearson's product-moment correlation
    ## 
    ## data:  mtcars$mpg and mtcars$wt
    ## t = -9.559, df = 30, p-value = 1.294e-10
    ## alternative hypothesis: true correlation is not equal to 0
    ## 95 percent confidence interval:
    ##  -0.9338264 -0.7440872
    ## sample estimates:
    ##        cor 
    ## -0.8676594

    # Spearman秩相关（单调相关）：数据不满足正态性或存在非线性单调关系。

    cor_spearman <- cor.test(mtcars$mpg, mtcars$wt, method = "spearman")

    ## Warning in cor.test.default(mtcars$mpg, mtcars$wt, method = "spearman"): Cannot
    ## compute exact p-value with ties

    print(cor_spearman)

    ## 
    ##  Spearman's rank correlation rho
    ## 
    ## data:  mtcars$mpg and mtcars$wt
    ## S = 10292, p-value = 1.488e-11
    ## alternative hypothesis: true rho is not equal to 0
    ## sample estimates:
    ##       rho 
    ## -0.886422

    # Kendall's Tau（有序数据或小样本）：样本量小或存在大量重复值。

    cor_kendall <- cor.test(mtcars$mpg, mtcars$wt, method = "kendall")

    ## Warning in cor.test.default(mtcars$mpg, mtcars$wt, method = "kendall"): Cannot
    ## compute exact p-value with ties

    print(cor_kendall)

    ## 
    ##  Kendall's rank correlation tau
    ## 
    ## data:  mtcars$mpg and mtcars$wt
    ## z = -5.7981, p-value = 6.706e-09
    ## alternative hypothesis: true tau is not equal to 0
    ## sample estimates:
    ##        tau 
    ## -0.7278321

    #  多变量相关性矩阵：分析数据框中多个变量的相关性：
    # 计算相关系数矩阵
    cor_matrix <- cor(mtcars[, c("mpg", "wt", "hp", "disp")], method = "pearson")
    print(cor_matrix)

    ##             mpg         wt         hp       disp
    ## mpg   1.0000000 -0.8676594 -0.7761684 -0.8475514
    ## wt   -0.8676594  1.0000000  0.6587479  0.8879799
    ## hp   -0.7761684  0.6587479  1.0000000  0.7909486
    ## disp -0.8475514  0.8879799  0.7909486  1.0000000

    # 可视化（热图）：红色表示负相关，蓝色表示正相关。
    library(corrplot)

    ## corrplot 0.95 loaded

    corrplot(cor_matrix, method = "color", type = "upper", tl.col = "black")

![](学习R_files/figure-markdown_strict/unnamed-chunk-36-1.png)

    # 偏相关分析（控制混杂变量）：在控制其他变量（如 hp）的条件下，分析 mpg 和 wt 的关系：
    library(ppcor)

    ## Loading required package: MASS

    pcor_test <- pcor.test(mtcars$mpg, mtcars$wt, mtcars[, "hp"])
    print(pcor_test) # 偏相关系数（estimate）和p值

    ##     estimate      p.value statistic  n gp  Method
    ## 1 -0.7512049 1.119647e-06 -6.128695 32  1 pearson

    # 可视化
    # 散点图+回归线
    library(ggplot2)
    ggplot(mtcars, aes(x = wt, y = mpg)) +
      geom_point() +
      geom_smooth(method = "lm", se = FALSE, color = "red") +
      labs(title = "Scatterplot with Pearson Correlation", 
           x = "Weight (1000 lbs)", y = "Miles per Gallon")

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-36-2.png)

    # 散点图矩阵
    pairs(mtcars[, c("mpg", "wt", "hp")], pch = 19, lower.panel = NULL)

![](学习R_files/figure-markdown_strict/unnamed-chunk-36-3.png)

## 4.3、回归分析

**回归分析**可以帮助你探索变量之间的因果关系或预测关系

线性回归、逻辑回归、其他回归模型（泊松回归、岭回归）

简单线性回归：用于分析**连续型因变量**与一个或多个自变量之间的关系。

-   **Coefficients（系数）**：

    -   **`Estimate`**：回归系数（斜率）。

    -   **`Std. Error`**：标准误。

    -   **`t value`**：t统计量。

    -   **`Pr(>|t|)`**：p值（**p &lt; 0.05** 表示显著）。

-   **R-squared**：模型解释的变异比例（0~1，越大越好）。

-   **F-statistic**：整体模型显著性。

<!-- -->

    # 使用R内置的 mtcars 数据集，预测每加仑英里数（mpg）与车重（wt）和马力（hp）的关系：
    data(mtcars)
    head(mtcars[, c("mpg", "wt", "hp")])

    ##                    mpg    wt  hp
    ## Mazda RX4         21.0 2.620 110
    ## Mazda RX4 Wag     21.0 2.875 110
    ## Datsun 710        22.8 2.320  93
    ## Hornet 4 Drive    21.4 3.215 110
    ## Hornet Sportabout 18.7 3.440 175
    ## Valiant           18.1 3.460 105

    # 简单线性回归
    # 拟合模型：mpg ~ wt
    model_lm <- lm(mpg ~ wt, data = mtcars) # 拟合模型
    summary(model_lm)

    ## 
    ## Call:
    ## lm(formula = mpg ~ wt, data = mtcars)
    ## 
    ## Residuals:
    ##     Min      1Q  Median      3Q     Max 
    ## -4.5432 -2.3647 -0.1252  1.4096  6.8727 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept)  37.2851     1.8776  19.858  < 2e-16 ***
    ## wt           -5.3445     0.5591  -9.559 1.29e-10 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 3.046 on 30 degrees of freedom
    ## Multiple R-squared:  0.7528, Adjusted R-squared:  0.7446 
    ## F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10

    # 可视化
    library(ggplot2)
    ggplot(mtcars, aes(x = wt, y = mpg)) +
      geom_point() +
      geom_smooth(method = "lm", se = FALSE, color = "red") +
      labs(title = "Linear Regression: mpg ~ wt")

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-37-1.png)

多元线性回归

    # 拟合模型：mpg ~ wt + hp
    model_lm_multi <- lm(mpg ~ wt + hp, data = mtcars)
    summary(model_lm_multi)

    ## 
    ## Call:
    ## lm(formula = mpg ~ wt + hp, data = mtcars)
    ## 
    ## Residuals:
    ##    Min     1Q Median     3Q    Max 
    ## -3.941 -1.600 -0.182  1.050  5.854 
    ## 
    ## Coefficients:
    ##             Estimate Std. Error t value Pr(>|t|)    
    ## (Intercept) 37.22727    1.59879  23.285  < 2e-16 ***
    ## wt          -3.87783    0.63273  -6.129 1.12e-06 ***
    ## hp          -0.03177    0.00903  -3.519  0.00145 ** 
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## Residual standard error: 2.593 on 29 degrees of freedom
    ## Multiple R-squared:  0.8268, Adjusted R-squared:  0.8148 
    ## F-statistic: 69.21 on 2 and 29 DF,  p-value: 9.109e-12

模型诊断

检查回归假设（线性、正态性、同方差性、无多重共线性）：

-   **残差 vs. 拟合值**：检查线性关系（应无趋势）。

-   **QQ图**：检查残差正态性（点应接近直线）。

-   **Scale-Location图**：检查同方差性（残差波动应均匀）。

-   **Cook’s距离**：检查异常值。

<!-- -->

    # 绘制诊断图
    # par(mfrow = c(2, 2))
    plot(model_lm_multi)

![](学习R_files/figure-markdown_strict/unnamed-chunk-39-1.png)![](学习R_files/figure-markdown_strict/unnamed-chunk-39-2.png)![](学习R_files/figure-markdown_strict/unnamed-chunk-39-3.png)![](学习R_files/figure-markdown_strict/unnamed-chunk-39-4.png)

多种共线性检验

    library(car)
    vif(model_lm_multi)  # 方差膨胀因子（VIF > 5 表示共线性严重）

    ##       wt       hp 
    ## 1.766625 1.766625

逻辑回归

用于分析**二分类因变量**（如0/1、Yes/No）与自变量的关系。

-   **Coefficients**：

    -   **`Estimate`**：对数几率比（log-odds）。

    -   **`Pr(>|z|)`**：p值（**p &lt; 0.05** 表示显著）。

-   **AIC**：模型拟合优度（越小越好）

<!-- -->

    # 使用 Titanic 数据集（需转换）为例

    library(titanic)
    data <- titanic_train[, c("Survived", "Age", "Fare", "Sex")]
    data <- na.omit(data)  # 去除缺失值
    head(data)

    ##   Survived Age    Fare    Sex
    ## 1        0  22  7.2500   male
    ## 2        1  38 71.2833 female
    ## 3        1  26  7.9250 female
    ## 4        1  35 53.1000 female
    ## 5        0  35  8.0500   male
    ## 7        0  54 51.8625   male

    # 拟合逻辑回归模型
    model_logit <- glm(Survived ~ Age + Fare + Sex, 
                       data = data, 
                       family = binomial(link = "logit"))
    summary(model_logit)

    ## 
    ## Call:
    ## glm(formula = Survived ~ Age + Fare + Sex, family = binomial(link = "logit"), 
    ##     data = data)
    ## 
    ## Coefficients:
    ##              Estimate Std. Error z value Pr(>|z|)    
    ## (Intercept)  0.934841   0.239101   3.910 9.24e-05 ***
    ## Age         -0.010570   0.006498  -1.627    0.104    
    ## Fare         0.012773   0.002696   4.738 2.16e-06 ***
    ## Sexmale     -2.347599   0.189956 -12.359  < 2e-16 ***
    ## ---
    ## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    ## 
    ## (Dispersion parameter for binomial family taken to be 1)
    ## 
    ##     Null deviance: 964.52  on 713  degrees of freedom
    ## Residual deviance: 716.07  on 710  degrees of freedom
    ## AIC: 724.07
    ## 
    ## Number of Fisher Scoring iterations: 5

    # 计算几率比
    exp(coef(model_logit))  # 几率比（OR > 1表示正影响）

    ## (Intercept)         Age        Fare     Sexmale 
    ##  2.54680790  0.98948613  1.01285487  0.09559845

    # 模型评估
    library(pROC)

    ## Type 'citation("pROC")' for a citation.

    ## 
    ## Attaching package: 'pROC'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     cov, smooth, var

    prob <- predict(model_logit, type = "response")
    roc_curve <- roc(data$Survived, prob)

    ## Setting levels: control = 0, case = 1

    ## Setting direction: controls < cases

    plot(roc_curve)  # ROC曲线

![](学习R_files/figure-markdown_strict/unnamed-chunk-41-1.png)

    auc(roc_curve)   # AUC值（0.5~1，越大越好）

    ## Area under the curve: 0.8253

    # 可视化
    ggplot(data, aes(x = Age, y = Survived)) +
      geom_point(alpha = 0.5) +
      geom_smooth(method = "glm", 
                  method.args = list(family = "binomial"), 
                  se = FALSE, color = "blue") +
      labs(title = "Logistic Regression: Survival ~ Age")

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-41-2.png)

其他模型：泊松回归、岭回归

**泊松回归（Poisson
Regression）：**适用于**计数型因变量**（如事件发生次数）：

**岭回归/套索回归（Ridge/Lasso
Regression）：**用于**高维数据**或**共线性较强**的情况：

    library(glmnet)

    ## Loading required package: Matrix

    ## 
    ## Attaching package: 'Matrix'

    ## The following objects are masked from 'package:tidyr':
    ## 
    ##     expand, pack, unpack

    ## Loaded glmnet 4.1-10

    x <- model.matrix(mpg ~ ., mtcars)[, -1]  # 自变量矩阵
    y <- mtcars$mpg                           # 因变量
    model_lasso <- glmnet(x, y, alpha = 1)    # alpha=1为Lasso，0为Ridge
    plot(model_lasso, xvar = "lambda")        # 变量选择路径

![](学习R_files/figure-markdown_strict/unnamed-chunk-42-1.png)

模型比较与选择

比较AIC BIC

    AIC(model_lm, model_lm_multi)  # AIC越小越好

    ##                df      AIC
    ## model_lm        3 166.0294
    ## model_lm_multi  4 156.6523

    BIC(model_lm, model_lm_multi)  # BIC越小越好

    ##                df      BIC
    ## model_lm        3 170.4266
    ## model_lm_multi  4 162.5153

交叉验证

    library(caret)

    ## Loading required package: lattice

    train_control <- trainControl(method = "cv", number = 10)  # 10折交叉验证
    model_cv <- train(mpg ~ wt + hp, data = mtcars, 
                      method = "lm", 
                      trControl = train_control)
    print(model_cv)

    ## Linear Regression 
    ## 
    ## 32 samples
    ##  2 predictor
    ## 
    ## No pre-processing
    ## Resampling: Cross-Validated (10 fold) 
    ## Summary of sample sizes: 28, 29, 29, 28, 28, 29, ... 
    ## Resampling results:
    ## 
    ##   RMSE      Rsquared   MAE     
    ##   2.498169  0.9072488  2.095205
    ## 
    ## Tuning parameter 'intercept' was held constant at a value of TRUE

## 

## 5、R可视化

### 5.1、ggplot2

ggplot2 是一个 R
包，用于通过数据可视化进行统计计算和数据表示。它遵循底层图形语法，即图形语法，其中包含某些规则和独立组件，可用于以各种格式表示数据。

ggplot2遵循图形语法：数据、图层、坐标系、主题

    # 以iris数据为例，演示ggplot2基本用法

    iris_visulization <- ggplot(iris,  # 指定数据集
                                aes(Sepal.Length,Petal.Length,colour = Species))+   # 绘制的图例和属性
      geom_point()+# 添加散点图
      labs(y='Petal Length(cm)',x = 'Sepal Length(cm)')+  # 修改、定义坐标轴标签
      ggtitle('iris_visulization')  # 定义图片标题


    print(iris_visulization)

![](学习R_files/figure-markdown_strict/unnamed-chunk-45-1.png)

在已定义图像添加内容

    # 在iris_visulization基础上添加

    # iris_visulization 添加文本
    iris_visulization + 
      annotate('text',x = 6.0,y = 4.0,label = 'mid')  + # 添加文本，第一个参数指定为text
      annotate("rect", xmin = 5, xmax = 7, ymin = 4, ymax = 6, alpha = .5) +   # 突出显示区域，第一个参数指定rect
      annotate("segment", x = 5, xend = 7, y = 4, yend = 5, colour = "black") # 添加片段，参数segment

![](学习R_files/figure-markdown_strict/unnamed-chunk-46-1.png)

### 使用坐标轴

    iris_visulization1 <- ggplot(iris,  # 指定数据集
                                aes(y = Sepal.Length,x = Petal.Length,colour = Species))+   # 绘制的图例和属性
      geom_point()+ # 添加散点图
      labs(y='Petal Length(cm)',x = 'Sepal Length(cm)')+  # 修改、定义坐标轴标签
      ggtitle('iris_visulization')  # 定义图片标题
    print(iris_visulization1)

![](学习R_files/figure-markdown_strict/unnamed-chunk-47-1.png)

### 使用图例

轴和图例统称为参考线。它们允许我们从图中读取观察值并根据原始值映射回去。图例键和刻度标签均由刻度线决定。图例和轴是根据绘图所需的相应比例和几何图形自动生成的。

    # 以iris为例
    library(ggplot2)
    data(iris)

    # 绘图
    pic <- ggplot(iris,aes(Sepal.Length,Petal.Length,colour = Species)) + 
      geom_point()
    print(pic)

![](学习R_files/figure-markdown_strict/unnamed-chunk-48-1.png)

更改图例

我们可以借助属性”legend.position”删除图例，并得到相应的输出 −

    pic + theme(legend.position = 'none')  # 删除图例

![](学习R_files/figure-markdown_strict/unnamed-chunk-49-1.png)

用属性”element\_blank()“隐藏图例的标题，

    pic + theme(legend.title = element_blank())  # 隐藏图例标题

![](学习R_files/figure-markdown_strict/unnamed-chunk-50-1.png)

更改图例位置，根据需要使用图例位置。此属性用于生成准确的绘图表示。

     #更改图例位置
    pic + theme(legend.position="top") # 图例在顶部

![](学习R_files/figure-markdown_strict/unnamed-chunk-51-1.png)

    pic + theme(legend.position="bottom")  # 图例在底部

![](学习R_files/figure-markdown_strict/unnamed-chunk-51-2.png)

更改图例的字体样式

    # 更改图例标题和文本字体样式
    # 图例标题
    pic + theme(legend.title = element_text(colour = "blue",  # 图例名称颜色
                                            size = 10,  face = "bold"))

![](学习R_files/figure-markdown_strict/unnamed-chunk-52-1.png)

    # 图例标签
    pic + theme(legend.text = element_text(colour = "red", # 图例标签的颜色
                                           size = 8,  face = "bold"))

![](学习R_files/figure-markdown_strict/unnamed-chunk-52-2.png)

ggplot2绘制散点图

散点图显示一个变量与另一个变量的关联程度。变量之间的关系称为相关性，通常用于统计方法

    # 以iris为例

    pic_iris <- ggplot(iris,aes(Sepal.Length,Petal.Length,
                                colour = Species)) + # colour 为点添加颜色
      geom_point() # 绘制散点图

    pic_iris

![](学习R_files/figure-markdown_strict/unnamed-chunk-53-1.png)

使用 geom\_point() 函数中名为 shape 的属性来更改点的形状

    # 修改点的形状
    pic_iris + geom_point(shape = 8)

![](学习R_files/figure-markdown_strict/unnamed-chunk-54-1.png)

建立变量之间的关系。

    # 使用geom_smooth函数的属性方法，使用lm方法，添加回归线
    ggplot(iris, aes(Sepal.Length, Petal.Length, colour=Species)) +
      geom_point(shape=1) +
      geom_smooth(method=lm) # 有助于重叠模式和创建所需变量的模式

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-55-1.png)

添加没有阴影置信区域的回归线（阴影区域表示置信区域以外的内容。）

    # 使用geom_smooth函数的属性方法，使用lm方法，添加回归线
    ggplot(iris, aes(Sepal.Length, Petal.Length, colour=Species)) +
      geom_point(shape=1) +
      geom_smooth(method=lm,se = F) # 传入参数se = F

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-56-1.png)

ggplot2绘制抖动图

抖动图包括可以描绘散点图的特殊效果。抖动只不过是一个随机值，它被分配给点以将它们分开

    ggplot(mpg, aes(cyl, hwy)) +
      geom_point() +
      geom_jitter(aes(colour = class))

![](学习R_files/figure-markdown_strict/unnamed-chunk-57-1.png)

ggplot2绘制条形图和直方图，计数图主要表现形式

条形图以矩形方式表示分类数据。条形可以垂直和水平绘制。高度或长度与图形中表示的值成比例。条形图的
x 轴和 y 轴指定包含在特定数据集中的类别。

直方图是一种条形图，它表示原始数据，并清晰地显示所述数据集的分布情况。

    # 条形计数图
    p <- ggplot(mpg,aes(x = factor(cyl),fill = cyl)) + 
      geom_bar()  # 创建条形图，它采用称为计数的统计值属性。
    p

![](学习R_files/figure-markdown_strict/unnamed-chunk-58-1.png)

直方图

geom\_histogram() 包含创建直方图所需的所有属性

     # 直方图计数图
    ggplot(data=mpg, aes(x=hwy)) +
        geom_histogram( col="red",  # 线条颜色
           fill="green",    # 填充颜色
           alpha = .2,
           binwidth = 5) 

![](学习R_files/figure-markdown_strict/unnamed-chunk-59-1.png)

堆叠条形图

ggplot2绘制饼图

饼图被视为圆形统计图，被分成多个切片来表示数值比例。

创建饼图

    # 加载模块
    library(ggplot2)

    # 来源：频率表
    df <- as.data.frame(table(mpg$class))  # 对mpg的class列的列联表，并转化为数据框
    colnames(df) <- c("class", "freq")
    print(df)

    ##        class freq
    ## 1    2seater    5
    ## 2    compact   47
    ## 3    midsize   41
    ## 4    minivan   11
    ## 5     pickup   33
    ## 6 subcompact   35
    ## 7        suv   62

    pie <- ggplot(df, aes(x = "", y=freq, fill = factor(class))) +
      geom_bar(width = 1, stat = "identity") +
      theme(axis.line = element_blank(),
         plot.title = element_text(hjust=0.5)) +
         labs(fill="class",
            x=NULL,
           y=NULL, 
            title="Pie Chart of class", # 图片名
            caption="Source: mpg")  # 注释
    pie

![](学习R_files/figure-markdown_strict/unnamed-chunk-61-1.png)

创建所需的饼图

    pie + coord_polar(theta = "y", start=0)

![](学习R_files/figure-markdown_strict/unnamed-chunk-62-1.png)

# ggplot2 - 边际图

边际图用于评估两个变量之间的关系并检查它们的分布。当我们谈到创建边际图时，它们只不过是在各自的
x 轴和 y 轴边缘具有直方图、箱线图或点图的散点图。

使用包”ggExtra”在 R 中创建边际图

    library(ggplot2,ggExtra)

    head(mpg)

    ## # A tibble: 6 × 11
    ##   manufacturer model displ  year   cyl trans      drv     cty   hwy fl    class 
    ##   <chr>        <chr> <dbl> <int> <int> <chr>      <chr> <int> <int> <chr> <chr> 
    ## 1 audi         a4      1.8  1999     4 auto(l5)   f        18    29 p     compa…
    ## 2 audi         a4      1.8  1999     4 manual(m5) f        21    29 p     compa…
    ## 3 audi         a4      2    2008     4 manual(m6) f        20    31 p     compa…
    ## 4 audi         a4      2    2008     4 auto(av)   f        21    30 p     compa…
    ## 5 audi         a4      2.8  1999     6 auto(l5)   f        16    26 p     compa…
    ## 6 audi         a4      2.8  1999     6 manual(m5) f        18    26 p     compa…

    # 绘图
    mpg_pic <- ggplot(mpg,aes(x = cty,y = hwy)) + 
      geom_count()+
      geom_smooth(method = 'lm',se = F)

    mpg_pic

    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-63-1.png)

使用 ggMarginal
函数创建边际图，这有助于生成两个属性”hwy”和”cty”之间的关系。

    library(ggExtra)
    ggMarginal(mpg_pic, type = "histogram", fill="transparent")  # 添加边际直方图

    ## `geom_smooth()` using formula = 'y ~ x'
    ## `geom_smooth()` using formula = 'y ~ x'

    ggMarginal(mpg_pic, type = "boxplot", fill="transparent")   # 添加边际箱图

    ## `geom_smooth()` using formula = 'y ~ x'
    ## `geom_smooth()` using formula = 'y ~ x'

![](学习R_files/figure-markdown_strict/unnamed-chunk-64-1.png)

# ggplot2 - 气泡图

气泡图其实就是散点图，它基本上是一个散点图，第三个数值变量用于表示圆圈大小。

绘制气泡图

    ggplot(mpg, aes(x=cty, y=hwy, size = displ)) + # size表示依据size的值定义气泡大小
      geom_point(alpha=0.7)+
      geom_smooth(method = 'lm',se = F)

    ## Warning: Using `size` aesthetic for lines was deprecated in ggplot2 3.4.0.
    ## ℹ Please use `linewidth` instead.
    ## This warning is displayed once every 8 hours.
    ## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
    ## generated.

    ## `geom_smooth()` using formula = 'y ~ x'

    ## Warning: The following aesthetics were dropped during statistical transformation: size.
    ## ℹ This can happen when ggplot fails to infer the correct grouping structure in
    ##   the data.
    ## ℹ Did you forget to specify a `group` aesthetic or to convert a numerical
    ##   variable into a factor?

![](学习R_files/figure-markdown_strict/unnamed-chunk-65-1.png)

# ggplot2 - 发散图

加载所需的包并在 mpg 数据集中创建一个名为”汽车名称”的新列。

    #Load ggplot 
    library(ggplot2) 

    # 为汽车名称创建新列 
    mtcars$`car name` <- rownames(mtcars) 

    # 计算标准化的 mtacrs
    mtcars$mpg_z <- round((mtcars$mpg - mean(mtcars$mpg))/sd(mtcars$mpg), 2) 

    # 高于/低于平均值标志 
    mtcars$mpg_type <- ifelse(mtcars$mpg_z < 0, "below", "above") 

    # sort 
    mtcars <- mtcars[order(mtcars$mpg_z), ]

    mtcars

    ##                      mpg cyl  disp  hp drat    wt  qsec vs am gear carb
    ## Cadillac Fleetwood  10.4   8 472.0 205 2.93 5.250 17.98  0  0    3    4
    ## Lincoln Continental 10.4   8 460.0 215 3.00 5.424 17.82  0  0    3    4
    ## Camaro Z28          13.3   8 350.0 245 3.73 3.840 15.41  0  0    3    4
    ## Duster 360          14.3   8 360.0 245 3.21 3.570 15.84  0  0    3    4
    ## Chrysler Imperial   14.7   8 440.0 230 3.23 5.345 17.42  0  0    3    4
    ## Maserati Bora       15.0   8 301.0 335 3.54 3.570 14.60  0  1    5    8
    ## Merc 450SLC         15.2   8 275.8 180 3.07 3.780 18.00  0  0    3    3
    ## AMC Javelin         15.2   8 304.0 150 3.15 3.435 17.30  0  0    3    2
    ## Dodge Challenger    15.5   8 318.0 150 2.76 3.520 16.87  0  0    3    2
    ## Ford Pantera L      15.8   8 351.0 264 4.22 3.170 14.50  0  1    5    4
    ## Merc 450SE          16.4   8 275.8 180 3.07 4.070 17.40  0  0    3    3
    ## Merc 450SL          17.3   8 275.8 180 3.07 3.730 17.60  0  0    3    3
    ## Merc 280C           17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
    ## Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1
    ## Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2
    ## Merc 280            19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
    ## Pontiac Firebird    19.2   8 400.0 175 3.08 3.845 17.05  0  0    3    2
    ## Ferrari Dino        19.7   6 145.0 175 3.62 2.770 15.50  0  1    5    6
    ## Mazda RX4           21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag       21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
    ## Hornet 4 Drive      21.4   6 258.0 110 3.08 3.215 19.44  1  0    3    1
    ## Volvo 142E          21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2
    ## Toyota Corona       21.5   4 120.1  97 3.70 2.465 20.01  1  0    3    1
    ## Datsun 710          22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
    ## Merc 230            22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
    ## Merc 240D           24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
    ## Porsche 914-2       26.0   4 120.3  91 4.43 2.140 16.70  0  1    5    2
    ## Fiat X1-9           27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
    ## Honda Civic         30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
    ## Lotus Europa        30.4   4  95.1 113 3.77 1.513 16.90  1  1    5    2
    ## Fiat 128            32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
    ## Toyota Corolla      33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
    ##                                car name mpg_z mpg_type
    ## Cadillac Fleetwood   Cadillac Fleetwood -1.61    below
    ## Lincoln Continental Lincoln Continental -1.61    below
    ## Camaro Z28                   Camaro Z28 -1.13    below
    ## Duster 360                   Duster 360 -0.96    below
    ## Chrysler Imperial     Chrysler Imperial -0.89    below
    ## Maserati Bora             Maserati Bora -0.84    below
    ## Merc 450SLC                 Merc 450SLC -0.81    below
    ## AMC Javelin                 AMC Javelin -0.81    below
    ## Dodge Challenger       Dodge Challenger -0.76    below
    ## Ford Pantera L           Ford Pantera L -0.71    below
    ## Merc 450SE                   Merc 450SE -0.61    below
    ## Merc 450SL                   Merc 450SL -0.46    below
    ## Merc 280C                     Merc 280C -0.38    below
    ## Valiant                         Valiant -0.33    below
    ## Hornet Sportabout     Hornet Sportabout -0.23    below
    ## Merc 280                       Merc 280 -0.15    below
    ## Pontiac Firebird       Pontiac Firebird -0.15    below
    ## Ferrari Dino               Ferrari Dino -0.06    below
    ## Mazda RX4                     Mazda RX4  0.15    above
    ## Mazda RX4 Wag             Mazda RX4 Wag  0.15    above
    ## Hornet 4 Drive           Hornet 4 Drive  0.22    above
    ## Volvo 142E                   Volvo 142E  0.22    above
    ## Toyota Corona             Toyota Corona  0.23    above
    ## Datsun 710                   Datsun 710  0.45    above
    ## Merc 230                       Merc 230  0.45    above
    ## Merc 240D                     Merc 240D  0.72    above
    ## Porsche 914-2             Porsche 914-2  0.98    above
    ## Fiat X1-9                     Fiat X1-9  1.20    above
    ## Honda Civic                 Honda Civic  1.71    above
    ## Lotus Europa               Lotus Europa  1.71    above
    ## Fiat 128                       Fiat 128  2.04    above
    ## Toyota Corolla           Toyota Corolla  2.29    above

将值转换为因子以保留特定图中的排序顺序

    # 转换为因子以保留图中的排序顺序。
    mtcars$`car name` <- factor(mtcars$`car name`, levels = mtcars$`car name`)

创建条形图

散条形图标记了一些维度成员相对于所述值指向向上或向下的方向。

发散条形图的输出如下所示，我们使用函数 geom\_bar 来创建条形图

    # 发散的条形图
    ggplot(mtcars, aes(x=`car name`, y=mpg_z, label=mpg_z)) +
      geom_bar(stat='identity', aes(fill=mpg_type), width=.5) +
      scale_fill_manual(name="Mileage",
         labels = c("Above Average", "Below Average"),
         values = c("above"="#00ba38", "below"="#f8766d")) +
     labs(subtitle="Normalised mileage from 'mtcars'",
         title= "Diverging Bars") +
      coord_flip()

![](学习R_files/figure-markdown_strict/unnamed-chunk-68-1.png)

发散帮帮糖图

只需更改要使用的函数，即 geom\_segment()，它有助于创建棒棒糖图。

    ggplot(mtcars, aes(x=`car name`, y=mpg_z, label=mpg_z)) +
     geom_point(stat='identity', fill="black", size=6) +
     geom_segment(aes(y = 0,
        x = `car name`,
        yend = mpg_z,
        xend = `car name`),
           color = "black") +
     geom_text(color="white", size=2) +
     labs(title="Diverging Lollipop Chart",
        subtitle="Normalized mileage from 'mtcars': Lollipop") +
     ylim(-2.5, 2.5) +
     coord_flip()

![](学习R_files/figure-markdown_strict/unnamed-chunk-69-1.png)

密度图

密度图是上述数据集中任何数值变量分布的图形表示。它使用核密度估计来显示变量的概率密度函数。

“ggplot2”包包含一个名为 geom\_density() 的函数来创建密度图。

    p <- ggplot(mpg, aes(cty)) +
      geom_density(aes(fill=factor(cyl)), alpha=0.8)
     p

![](学习R_files/figure-markdown_strict/unnamed-chunk-70-1.png)

箱线图

箱线图也称为箱须图，表示数据的五个数字摘要。五个数字摘要包括最小值、第一四分位数、中位数、第三四分位数和最大值等值。穿过箱线图中间部分的垂直线被视为”中位数”。

    p <- ggplot(mpg, aes(class, cty)) +
      geom_boxplot(varwidth=T, fill="blue")
    p + labs(title="A Box plot Example",
        subtitle="Mileage by Class",
        caption="MPG Dataset",
        x="Class",
        y="Mileage")

![](学习R_files/figure-markdown_strict/unnamed-chunk-71-1.png)

    p

![](学习R_files/figure-markdown_strict/unnamed-chunk-71-2.png)

点图

点图类似于散点图，只是维度不同。在本节中，我们将在现有的箱线图中添加点图，以获得更好的图像和清晰度。

    p <- ggplot(mpg, aes(manufacturer, cty)) +
     geom_boxplot() +
     theme(axis.text.x = element_text(angle=65, vjust=0.6))
    p

![](学习R_files/figure-markdown_strict/unnamed-chunk-72-1.png)

小提琴图

    p <- ggplot(mpg, aes(class, cty))

    p + geom_violin()

![](学习R_files/figure-markdown_strict/unnamed-chunk-73-1.png)

设置背景颜色

命令更改背景颜色，这有助于更改面板 (panel.background) −

    ggplot(iris, aes(Sepal.Length, Species))+
      geom_point(color="firebrick")+
     theme(panel.background = element_rect(fill = 'white'),
           axis.line = element_line(color = 'black'))

![](学习R_files/figure-markdown_strict/unnamed-chunk-74-1.png)

## 6、R数据清洗

    library(readxl)
    files <- "A:\\Rstudio\\学习R\\学习R_数据\\第九批_AF.xlsx"

    dt <- read_excel(files)

    head(dt,5)

    ## # A tibble: 5 × 5
    ##   image_id index ID       label      detection
    ##   <chr>    <chr> <chr>    <chr>      <chr>    
    ## 1 图像_01  1a    HS120597 HS120597_1 42       
    ## 2 图像_01  1b    HS120597 HS120597_2 52       
    ## 3 图像_01  1c    HS120597 HS120597_3 61       
    ## 4 图像_01  1d    HS120597 HS120597_4 60       
    ## 5 图像_01  1e    HS120597 HS120597_5 54

删除含有缺失值的行

    library(dplyr)

    ## 
    ## Attaching package: 'dplyr'

    ## The following object is masked from 'package:MASS':
    ## 
    ##     select

    ## The following object is masked from 'package:car':
    ## 
    ##     recode

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

    dt_omit <- dt %>% na.omit()

删除重复行

    dt_repeat <- dt_omit %>% distinct(.keep_all = T)

删除某列中值为NaN的行

    dt_repeat

    ## # A tibble: 428 × 5
    ##    image_id index ID       label      detection
    ##    <chr>    <chr> <chr>    <chr>      <chr>    
    ##  1 图像_01  1a    HS120597 HS120597_1 42       
    ##  2 图像_01  1b    HS120597 HS120597_2 52       
    ##  3 图像_01  1c    HS120597 HS120597_3 61       
    ##  4 图像_01  1d    HS120597 HS120597_4 60       
    ##  5 图像_01  1e    HS120597 HS120597_5 54       
    ##  6 图像_02  2a    HS120599 HS120599_1 210      
    ##  7 图像_02  2b    HS120599 HS120599_2 126      
    ##  8 图像_02  2c    HS120599 HS120599_3 162      
    ##  9 图像_02  2d    HS120599 HS120599_4 209      
    ## 10 图像_02  2e    HS120599 HS120599_5 146      
    ## # ℹ 418 more rows

    # 删除某列中值为NaN的行
    dt_clear <- dt_repeat %>% 
      filter(detection != 'NaN')

    #同时 删除某列中值为NaN、a的行
    dt_clear <- dt_repeat %>% 
      filter(detection %in% c('a','NaN'))  # detection为列名

一个Excel文件多个sheet一次性读取，存为列表，方便访问、批处理

以A:\学习R\_数据下的rna\_seq.xlsx文件为例

    path = 'A:\\Rstudio\\学习R\\学习R_数据'
    setwd(path)

    library(rio)

    # 读取所有Sheet到列表
    RNA_seq <- import_list("RNA_seq.xlsx")

    # 自动命名列表元素（Sheet名）
    names(RNA_seq) <- excel_sheets("RNA_seq.xlsx")

将一个excel的多个sheet横向合并,**指定列**

如果多个Sheet需要按某一列（如样本ID）对齐后再横向合并：

    path = 'A:\\Rstudio\\学习R\\学习R_数据'
    setwd(path)

    # 加载包
    library(readxl)
    library(dplyr)
    library(purrr)

    ## 
    ## Attaching package: 'purrr'

    ## The following object is masked from 'package:caret':
    ## 
    ##     lift

    ## The following object is masked from 'package:car':
    ## 
    ##     some

    file <- 'RNA_seq.xlsx'

    # 1. 读取Excel中的所有Sheet名称
    sheet_names <- excel_sheets(file)

    # 2. 读取所有Sheet到列表
    RNA_dt <- map(sheet_names, ~ read_excel(file, sheet = .x))

    # 假设所有Sheet都有"ID"列
    merged_data <- reduce(RNA_dt, ~ full_join(.x, .y, by = "gene_id"))

    # 或使用左连接（以第一个Sheet的ID为准）,只保留第一个sheet的ID，其他sheet的ID删除
    merged_data <- reduce(RNA_dt, ~ left_join(.x, .y, by = "gene_id"))

    head(merged_data)

    ## # A tibble: 6 × 5
    ##   gene_id   chicken_liver_A_counts chicken_liver_B_counts chicken_muscle_A_cou…¹
    ##   <chr>                      <dbl>                  <dbl>                  <dbl>
    ## 1 ENSGALG0…                      1                      3                      3
    ## 2 ENSGALG0…                    366                    609                   1162
    ## 3 ENSGALG0…                      0                      0                      0
    ## 4 ENSGALG0…                      0                      0                      0
    ## 5 ENSGALG0…                     36                     30                    167
    ## 6 ENSGALG0…                   1740                   2414                   4007
    ## # ℹ abbreviated name: ¹​chicken_muscle_A_counts
    ## # ℹ 1 more variable: chicken_muscle_B_counts <dbl>

合并两个数据框，指定列

    data_1 <- head(RNA_seq$chicken_liver_A_counts,10)
    data_2 <- head(RNA_seq$chicken_muscle_A_counts,15)

保留两个数据框中关键列匹配的行

    library(dplyr)

    # 按指定列（如"ID"）合并，仅保留共有的行
    data_same <- inner_join(data_1, data_2, by = "gene_id")

    # 多列作为关键列
    # merged_data <- inner_join(data_1, data_2, by = c("ID", "Date"))

    head(data_same)

    ##              gene_id chicken_liver_A_counts chicken_muscle_A_counts
    ## 1 ENSGALG00000000003                      1                       3
    ## 2 ENSGALG00000000011                    366                    1162
    ## 3 ENSGALG00000000038                      0                       0
    ## 4 ENSGALG00000000044                      0                       0
    ## 5 ENSGALG00000000048                     36                     167
    ## 6 ENSGALG00000000055                   1740                    4007

**保留左边**数据框的所有行，匹配右边数据框的列，只保留df1有的行

    # 保留df1的所有行，df2无匹配时填充NA
    data_all_1 <- left_join(data_1,data_2,by = 'gene_id')
    head(data_all_1)

    ##              gene_id chicken_liver_A_counts chicken_muscle_A_counts
    ## 1 ENSGALG00000000003                      1                       3
    ## 2 ENSGALG00000000011                    366                    1162
    ## 3 ENSGALG00000000038                      0                       0
    ## 4 ENSGALG00000000044                      0                       0
    ## 5 ENSGALG00000000048                     36                     167
    ## 6 ENSGALG00000000055                   1740                    4007

保留两个数据框的所有行，无匹配时填充NA

    data_all <- full_join(data_1,data_2,by = 'gene_id')
    head(data_all,15)

    ##               gene_id chicken_liver_A_counts chicken_muscle_A_counts
    ## 1  ENSGALG00000000003                      1                       3
    ## 2  ENSGALG00000000011                    366                    1162
    ## 3  ENSGALG00000000038                      0                       0
    ## 4  ENSGALG00000000044                      0                       0
    ## 5  ENSGALG00000000048                     36                     167
    ## 6  ENSGALG00000000055                   1740                    4007
    ## 7  ENSGALG00000000059                      8                       6
    ## 8  ENSGALG00000000067                   3818                     105
    ## 9  ENSGALG00000000071                    130                     130
    ## 10 ENSGALG00000000081                     19                       2
    ## 11 ENSGALG00000000086                     NA                    5473
    ## 12 ENSGALG00000000091                     NA                     874
    ## 13 ENSGALG00000000094                     NA                    3194
    ## 14 ENSGALG00000000102                     NA                      17
    ## 15 ENSGALG00000000104                     NA                      43

**保留右边**数据框的所有行，匹配左边数据框的列,Na填充左边没有

    data_all_2 <- right_join(data_1,data_2,by = 'gene_id')
    head(data_all_2,15)

    ##               gene_id chicken_liver_A_counts chicken_muscle_A_counts
    ## 1  ENSGALG00000000003                      1                       3
    ## 2  ENSGALG00000000011                    366                    1162
    ## 3  ENSGALG00000000038                      0                       0
    ## 4  ENSGALG00000000044                      0                       0
    ## 5  ENSGALG00000000048                     36                     167
    ## 6  ENSGALG00000000055                   1740                    4007
    ## 7  ENSGALG00000000059                      8                       6
    ## 8  ENSGALG00000000067                   3818                     105
    ## 9  ENSGALG00000000071                    130                     130
    ## 10 ENSGALG00000000081                     19                       2
    ## 11 ENSGALG00000000086                     NA                    5473
    ## 12 ENSGALG00000000091                     NA                     874
    ## 13 ENSGALG00000000094                     NA                    3194
    ## 14 ENSGALG00000000102                     NA                      17
    ## 15 ENSGALG00000000104                     NA                      43

保留左边数据框中与右边匹配的行，不合并右边列，保留左边数据框中出现在右边的行

    # 筛选df1中存在于df2的行
    filtered_data <- semi_join(data_1,data_2,by = 'gene_id')

保留左边数据框中与右边不匹配的行

    # 筛选df1中不存在于df2的行
    filtered_data_a <- anti_join(data_2,data_1,by = 'gene_id')

选出某列的值为a的行

    library(tidyr)
    head(iris)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    setosa <- iris %>% 
      filter(Species == 'setosa')  # 筛选出species列中是setosa的行
    setosa

    ##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1           5.1         3.5          1.4         0.2  setosa
    ## 2           4.9         3.0          1.4         0.2  setosa
    ## 3           4.7         3.2          1.3         0.2  setosa
    ## 4           4.6         3.1          1.5         0.2  setosa
    ## 5           5.0         3.6          1.4         0.2  setosa
    ## 6           5.4         3.9          1.7         0.4  setosa
    ## 7           4.6         3.4          1.4         0.3  setosa
    ## 8           5.0         3.4          1.5         0.2  setosa
    ## 9           4.4         2.9          1.4         0.2  setosa
    ## 10          4.9         3.1          1.5         0.1  setosa
    ## 11          5.4         3.7          1.5         0.2  setosa
    ## 12          4.8         3.4          1.6         0.2  setosa
    ## 13          4.8         3.0          1.4         0.1  setosa
    ## 14          4.3         3.0          1.1         0.1  setosa
    ## 15          5.8         4.0          1.2         0.2  setosa
    ## 16          5.7         4.4          1.5         0.4  setosa
    ## 17          5.4         3.9          1.3         0.4  setosa
    ## 18          5.1         3.5          1.4         0.3  setosa
    ## 19          5.7         3.8          1.7         0.3  setosa
    ## 20          5.1         3.8          1.5         0.3  setosa
    ## 21          5.4         3.4          1.7         0.2  setosa
    ## 22          5.1         3.7          1.5         0.4  setosa
    ## 23          4.6         3.6          1.0         0.2  setosa
    ## 24          5.1         3.3          1.7         0.5  setosa
    ## 25          4.8         3.4          1.9         0.2  setosa
    ## 26          5.0         3.0          1.6         0.2  setosa
    ## 27          5.0         3.4          1.6         0.4  setosa
    ## 28          5.2         3.5          1.5         0.2  setosa
    ## 29          5.2         3.4          1.4         0.2  setosa
    ## 30          4.7         3.2          1.6         0.2  setosa
    ## 31          4.8         3.1          1.6         0.2  setosa
    ## 32          5.4         3.4          1.5         0.4  setosa
    ## 33          5.2         4.1          1.5         0.1  setosa
    ## 34          5.5         4.2          1.4         0.2  setosa
    ## 35          4.9         3.1          1.5         0.2  setosa
    ## 36          5.0         3.2          1.2         0.2  setosa
    ## 37          5.5         3.5          1.3         0.2  setosa
    ## 38          4.9         3.6          1.4         0.1  setosa
    ## 39          4.4         3.0          1.3         0.2  setosa
    ## 40          5.1         3.4          1.5         0.2  setosa
    ## 41          5.0         3.5          1.3         0.3  setosa
    ## 42          4.5         2.3          1.3         0.3  setosa
    ## 43          4.4         3.2          1.3         0.2  setosa
    ## 44          5.0         3.5          1.6         0.6  setosa
    ## 45          5.1         3.8          1.9         0.4  setosa
    ## 46          4.8         3.0          1.4         0.3  setosa
    ## 47          5.1         3.8          1.6         0.2  setosa
    ## 48          4.6         3.2          1.4         0.2  setosa
    ## 49          5.3         3.7          1.5         0.2  setosa
    ## 50          5.0         3.3          1.4         0.2  setosa

根据某列的值的大小范围进行筛选

    head(iris)

    ##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
    ## 1          5.1         3.5          1.4         0.2  setosa
    ## 2          4.9         3.0          1.4         0.2  setosa
    ## 3          4.7         3.2          1.3         0.2  setosa
    ## 4          4.6         3.1          1.5         0.2  setosa
    ## 5          5.0         3.6          1.4         0.2  setosa
    ## 6          5.4         3.9          1.7         0.4  setosa

    petal_len_less <- iris %>%
      filter(Petal.Length < 1.5)  # 筛选Petal.Length小于1.5的行

    nrow(petal_len_less)

    ## [1] 24
