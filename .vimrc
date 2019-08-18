set number " 设置行号
:set vb t_vb= " 取消提示声音
set tabstop=4     " 设置tab为4个空格
set softtabstop=4 " 表示在编辑模式的时候按退格键的时候退回缩进的长度
set shiftwidth=4  " 表示每一级缩进的长度，一般设置成跟 softtabstop 一样
set expandtab     " 表示缩进用空格来表示，noexpandtab 则是用制表符表示一个缩进
set autoindent    " 自动缩进
" 窗口的切换
noremap <C-h> <C-w>h
noremap <C-j> <C-w>j
noremap <C-k> <C-w>k
noremap <C-l> <C-w>l
noremap <F3> :NERDTreeToggle <CR> " 打开目录树
noremap <F4> :Autoformat<CR> " 按F4代码格式化

call plug#begin('~/.vim/plugged')
Plug 'mhinz/vim-startify' " vim初始页面
Plug 'dense-analysis/ale' " 错误提示
Plug 'Chiel92/vim-autoformat' " 代码格式化
Plug 'itchyny/vim-cursorword' " 光标所在单词下划线
Plug 'lfv89/vim-interestingwords' " 选中的单词高亮
Plug 'scrooloose/nerdtree'        " 目录树
call plug#end()


"定义CompileRun函数，用来调用进行编译和运行
map <F5> :call CompileRun()<CR>
map <C-F5> :call Debug()<CR>
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
" 调试函数
func! Debug()
    exec "w"
    if &filetype == "c"
        exec "!gcc % -o %< -gstabs+"
        exec "!gdb %<"
    elseif &filetype == "cpp"
        exec "!g++ % -o %< -gstabs+"
        exec "!gdb %<"
    endif
endfunc
