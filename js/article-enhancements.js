// Smith Ribbon Article Enhancement Script
// 添加面包屑导航和社交媒体分享功能

// 文章信息配置
const articleInfo = {
    'news4.html': {
        title: '织带在礼品包装中的艺术应用',
        enTitle: 'Artistic Application of Ribbons in Gift Packaging',
        description: '在送礼文化日益精致的今天，礼品包装已经成为表达心意的重要组成部分。本文将深入探讨织带在礼品包装中的应用技巧。',
        enDescription: 'In today\'s increasingly refined gift-giving culture, gift packaging has become an important part of expressing care.',
        category: '礼品包装',
        enCategory: 'Gift Packaging'
    },
    'news5.html': {
        title: '如何选择高品质的印刷织带：专业采购指南',
        enTitle: 'How to Choose High-Quality Printed Ribbons: Professional Procurement Guide',
        description: '在当今竞争激烈的商业环境中，个性化定制已成为品牌差异化营销的重要手段。本文提供专业的印刷织带选购指南。',
        enDescription: 'In today\'s competitive business environment, personalized customization has become important for brand differentiation.',
        category: '产品选购',
        enCategory: 'Product Selection'
    },
    'news6.html': {
        title: '蝴蝶结装饰指南：让家居和婚礼更添浪漫',
        enTitle: 'Bow Decoration Guide: Adding Romance to Home and Weddings',
        description: '蝴蝶结作为经典优雅的装饰元素，广泛应用于婚礼和家居装饰中。本文将深入探讨蝴蝶结的应用技巧。',
        enDescription: 'As a classic and elegant decorative element, bows are widely used in wedding and home decoration.',
        category: '装饰技巧',
        enCategory: 'Decoration Tips'
    }
};

// 添加面包屑导航
function addBreadcrumb() {
    const currentPage = window.location.pathname.split('/').pop() || 'news4.html';
    const info = articleInfo[currentPage] || articleInfo['news4.html'];
    
    const isZh = document.body.classList.contains('lang-zh') || 
                 document.documentElement.lang === 'zh-CN' ||
                 !document.body.classList.contains('lang-en');
    
    const breadcrumbHTML = `
        <style>
            .breadcrumb-nav {
                background: #f8f9fa;
                padding: 15px 20px;
                border-bottom: 1px solid #eee;
                font-size: 14px;
            }
            
            .breadcrumb-nav-container {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .breadcrumb-nav a {
                color: #1a5f7a;
                text-decoration: none;
                transition: color 0.3s;
            }
            
            .breadcrumb-nav a:hover {
                color: #159895;
            }
            
            .breadcrumb-nav span {
                color: #666;
            }
            
            .breadcrumb-nav .current {
                color: #999;
                font-weight: 500;
            }
            
            .breadcrumb-nav .separator {
                color: #ccc;
                margin: 0 5px;
            }
            
            /* 社交分享按钮样式 */
            .social-share {
                display: flex;
                gap: 10px;
                margin: 30px 0;
                padding: 20px 0;
                border-top: 1px solid #eee;
                border-bottom: 1px solid #eee;
            }
            
            .share-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 45px;
                height: 45px;
                border-radius: 50%;
                color: white;
                font-size: 20px;
                text-decoration: none;
                transition: all 0.3s;
                cursor: pointer;
                border: none;
            }
            
            .share-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }
            
            .share-btn.wechat { background: #07c160; }
            .share-btn.weibo { background: #e6162d; }
            .share-btn.qq { background: #12b7f5; }
            .share-btn.facebook { background: #1877f2; }
            .share-btn.twitter { background: #1da1f2; }
            .share-btn.linkedin { background: #0077b5; }
            
            .share-label {
                font-size: 14px;
                color: #666;
                margin-right: 15px;
                font-weight: 500;
            }
            
            /* 文章顶部元信息 */
            .article-meta-enhanced {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 2px solid #eee;
                flex-wrap: wrap;
                gap: 15px;
            }
            
            .article-categories {
                display: flex;
                gap: 10px;
            }
            
            .category-tag {
                padding: 6px 16px;
                background: linear-gradient(135deg, #1a5f7a, #159895);
                color: white;
                border-radius: 20px;
                font-size: 13px;
                font-weight: 500;
            }
            
            .article-tags {
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
            }
            
            .tag {
                padding: 4px 12px;
                background: #f0f0f0;
                color: #666;
                border-radius: 15px;
                font-size: 12px;
            }
        </style>
        
        <!-- 面包屑导航 -->
        <div class="breadcrumb-nav">
            <div class="breadcrumb-nav-container">
                <a href="index.html">🏠 <span class="zh-content">首页</span><span class="en-content">Home</span></a>
                <span class="separator">›</span>
                <a href="blog.html">📚 <span class="zh-content">博客</span><span class="en-content">Blog</span></a>
                <span class="separator">›</span>
                <span class="current">${isZh ? info.title : info.enTitle}</span>
            </div>
        </div>
    `;
    
    // 在header后插入面包屑导航
    const header = document.querySelector('header');
    if (header) {
        header.insertAdjacentHTML('afterend', breadcrumbHTML);
    }
    
    // 修改文章头部区域
    const articleHeader = document.querySelector('.article-header');
    if (articleHeader) {
        const metaHTML = `
            <div class="article-meta-enhanced">
                <div class="article-categories">
                    <span class="category-tag">${isZh ? info.category : info.enCategory}</span>
                </div>
                <div class="article-tags">
                    <span class="tag">${isZh ? '织带' : 'Ribbon'}</span>
                    <span class="tag">${isZh ? info.category : info.enCategory}</span>
                    <span class="tag">Smith Ribbon</span>
                </div>
            </div>
        `;
        articleHeader.insertAdjacentHTML('afterbegin', metaHTML);
    }
    
    // 添加社交分享按钮
    addSocialShareButtons();
}

// 添加社交分享按钮
function addSocialShareButtons() {
    const currentUrl = window.location.href;
    const currentPage = window.location.pathname.split('/').pop() || 'news4.html';
    const info = articleInfo[currentPage] || articleInfo['news4.html'];
    
    const isZh = document.body.classList.contains('lang-zh') || 
                 document.documentElement.lang === 'zh-CN' ||
                 !document.body.classList.contains('lang-en');
    
    const shareText = isZh ? info.description : info.enDescription;
    const encodedUrl = encodeURIComponent(currentUrl);
    const encodedText = encodeURIComponent(shareText);
    
    const shareHTML = `
        <!-- 社交分享按钮 -->
        <div class="social-share">
            <span class="share-label">${isZh ? '分享到:' : 'Share:'}</span>
            <button class="share-btn wechat" onclick="shareToWechat('${encodedUrl}', '${encodedText}')" title="${isZh ? '微信' : 'WeChat'}">
                💬
            </button>
            <button class="share-btn weibo" onclick="shareToWeibo('${encodedUrl}', '${encodedText}')" title="${isZh ? '微博' : 'Weibo'}">
                📢
            </button>
            <button class="share-btn qq" onclick="shareToQQ('${encodedUrl}', '${encodedText}')" title="QQ">
                💬
            </button>
            <button class="share-btn facebook" onclick="shareToFacebook('${encodedUrl}')" title="Facebook">
                👍
            </button>
            <button class="share-btn twitter" onclick="shareToTwitter('${encodedUrl}', '${encodedText}')" title="Twitter">
                🐦
            </button>
            <button class="share-btn linkedin" onclick="shareToLinkedIn('${encodedUrl}')" title="LinkedIn">
                💼
            </button>
        </div>
        
        <!-- 微信分享弹窗 -->
        <div id="wechat-share-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:10000;align-items:center;justify-content:center;">
            <div style="background:white;padding:30px;border-radius:15px;max-width:400px;text-align:center;position:relative;">
                <button onclick="closeWechatModal()" style="position:absolute;top:10px;right:10px;border:none;background:none;font-size:24px;cursor:pointer;">✕</button>
                <h3 style="margin-bottom:20px;">${isZh ? '分享到微信' : 'Share to WeChat'}</h3>
                <div id="wechat-qrcode" style="margin:20px 0;"></div>
                <p style="color:#666;font-size:14px;">${isZh ? '扫描二维码分享' : 'Scan QR code to share'}</p>
            </div>
        </div>
    `;
    
    // 在作者信息前插入分享按钮
    const authorInfo = document.querySelector('.author-info');
    if (authorInfo) {
        authorInfo.insertAdjacentHTML('beforebegin', shareHTML);
    }
}

// 分享函数
function shareToWechat(url, text) {
    const modal = document.getElementById('wechat-share-modal');
    if (modal) {
        modal.style.display = 'flex';
        // 这里可以集成二维码生成API
        document.getElementById('wechat-qrcode').innerHTML = `
            <div style="width:200px;height:200px;background:#f0f0f0;margin:0 auto;display:flex;align-items:center;justify-content:center;">
                <span style="font-size:48px;">📱</span>
            </div>
        `;
    }
}

function closeWechatModal() {
    const modal = document.getElementById('wechat-share-modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

function shareToWeibo(url, text) {
    const weiboUrl = `https://service.weibo.com/share/share.php?url=${url}&title=${text}`;
    window.open(weiboUrl, '_blank', 'width=600,height=400');
}

function shareToQQ(url, text) {
    const qqUrl = `https://connect.qq.com/widget/shareqq/index.html?url=${url}&title=${document.title}&pics=${encodeURIComponent('https://smithribbon.com/images/logo.png')}`;
    window.open(qqUrl, '_blank', 'width=600,height=400');
}

function shareToFacebook(url) {
    const fbUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
    window.open(fbUrl, '_blank', 'width=600,height=400');
}

function shareToTwitter(url, text) {
    const twitterUrl = `https://twitter.com/intent/tweet?url=${url}&text=${text}`;
    window.open(twitterUrl, '_blank', 'width=600,height=400');
}

function shareToLinkedIn(url) {
    const linkedInUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${url}`;
    window.open(linkedInUrl, '_blank', 'width=600,height=400');
}

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    // 延迟执行确保DOM完全加载
    setTimeout(addBreadcrumb, 100);
});

// 监听语言切换
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('lang-btn')) {
        setTimeout(addBreadcrumb, 200);
    }
});
