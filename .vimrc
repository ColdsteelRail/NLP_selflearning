set number " 设置行号
:set vb t_vb= " 取消提示声音
set tabstop=4     " 设置tab为4个空格
set softtabstop=4 " 表示在编辑模式的时候按退格键的时候退回缩进的长度
set shiftwidth=4  " 表示每一级缩进的长度，一般设置成跟 softtabstop 一样
set expandtab     " 表示缩进用空格来表示，noexpandtab 则是用制表符表示一个缩进
set autoindent    " 自动缩进
syntax enable
set background=dark
set nocompatible
" 窗口的切换
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l
noremap <F3> :NERDTreeToggle <CR> " 打开目录树
noremap <F4> :Autoformat<CR>:w<CR> " 代码格式化并且保存
noremap <F2> :TlistOpen<CR>  "打开函数列表

"插件管理
call plug#begin('~/.vim/plugged')
Plug 'mhinz/vim-startify' " vim初始页面
Plug 'dense-analysis/ale' " 错误提示
Plug 'Chiel92/vim-autoformat' " 代码格式化
Plug 'itchyny/vim-cursorword' " 光标所在单词下划线
Plug 'lfv89/vim-interestingwords' " 选中的单词高亮
Plug 'scrooloose/nerdtree'        " 目录树
Plug 'jiangmiao/auto-pairs'       " 括号自动匹配
Plug 'justmao945/vim-clang'       " cpp/c自动补齐
Plug 'ervandew/supertab'          " 函数变量自动补齐
Plug 'vim-scripts/taglist.vim'    " 显示函数变量列表
call plug#end()
"taglist设置
let Tlist_Use_Right_Window=1
let Tlist_Exit_OnlyWindow=1

"定义CompileRun函数，用来调用进行编译和运行
map <F5> :call CompileRun()<CR>
" 编译函数
func! CompileRun()
    exec "w"
    if &filetype == "c"
        exec "!gcc % -o %<"
        exec "!./%<"
    elseif &filetype == "cpp"
        exec "!g++ % -o %<"
        exec "!./%<"
    endif
endfunc

