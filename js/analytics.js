/**
 * Smith Ribbon Analytics & SEO Monitoring
 * 网站流量监控与搜索引擎排名追踪
 */

// Google Analytics Configuration - 请替换为您的GA4 Measurement ID
const GA_TRACKING_ID = 'G-XXXXXXXXXX';

// Initialize Google Analytics
function initAnalytics() {
    // Load Google Analytics script
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${GA_TRACKING_ID}`;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', GA_TRACKING_ID, {
        'send_page_view': true,
        'anonymize_ip': true
    });
    
    console.log('✅ Google Analytics initialized');
}

// Track Page Views
function trackPageView(pageUrl, pageTitle) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'page_view', {
            'page_title': pageTitle,
            'page_location': pageUrl
        });
    }
    console.log(`📊 Page view tracked: ${pageTitle}`);
}

// Track Article Views
function trackArticleView(articleTitle, articleCategory) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'article_view', {
            'event_category': 'Article',
            'event_label': articleTitle,
            'value': 1
        });
    }
    console.log(`📄 Article tracked: ${articleTitle} (${articleCategory})`);
}

// Track Social Shares
function trackShare(platform, articleTitle) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'share', {
            'event_category': 'Social',
            'event_label': `${platform}: ${articleTitle}`
        });
    }
    console.log(`📤 Shared: ${articleTitle} to ${platform}`);
}

// Track Product Clicks
function trackProductClick(productName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'select_content', {
            'content_type': 'Product',
            'item_id': productName
        });
    }
    console.log(`🛒 Product click: ${productName}`);
}

// SEO Performance Monitoring Dashboard
const SEOMonitor = {
    // Store tracking data locally
    data: {
        pageViews: {},
        articleReads: {},
        socialShares: {},
        productClicks: {},
        keywords: {
            '织带': 0,
            '印刷织带': 0,
            '礼品包装': 0,
            '蝴蝶结': 0,
            '缎带': 0,
            'ribbon manufacturer': 0,
            'printed ribbon': 0
        }
    },
    
    // Initialize monitoring
    init() {
        console.log('🔍 SEO Monitor initialized');
        this.loadStoredData();
        this.setupAutoTracking();
        
        // Setup share tracking
        this.setupShareTracking();
    },
    
    // Load stored data from localStorage
    loadStoredData() {
        const stored = localStorage.getItem('smithribbon_seo_data');
        if (stored) {
            this.data = JSON.parse(stored);
        }
    },
    
    // Save data to localStorage
    saveData() {
        localStorage.setItem('smithribbon_seo_data', JSON.stringify(this.data));
    },
    
    // Track page view
    trackPageView(pageUrl, pageTitle) {
        this.data.pageViews[pageUrl] = (this.data.pageViews[pageUrl] || 0) + 1;
        this.saveData();
        this.updateSEOScore(pageUrl);
    },
    
    // Update SEO score based on elements
    updateSEOScore(pageUrl) {
        let score = 0;
        const pageViews = this.data.pageViews[pageUrl] || 0;
        
        // Score based on page views
        if (pageViews > 100) score += 30;
        else if (pageViews > 50) score += 20;
        else if (pageViews > 10) score += 10;
        
        // Check for SEO elements
        const hasMetaDesc = document.querySelector('meta[name="description"]');
        const hasKeywords = document.querySelector('meta[name="keywords"]');
        const hasOGTags = document.querySelector('meta[property^="og:"]');
        const hasCanonical = document.querySelector('link[rel="canonical"]');
        const hasSchema = document.querySelector('script[type="application/ld+json"]');
        
        if (hasMetaDesc) score += 15;
        if (hasKeywords) score += 10;
        if (hasOGTags) score += 15;
        if (hasCanonical) score += 10;
        if (hasSchema) score += 20;
        
        return Math.min(score, 100); // Max 100
    },
    
    // Setup automatic tracking
    setupAutoTracking() {
        // Track initial page view
        window.addEventListener('load', () => {
            this.trackPageView(window.location.href, document.title);
        });
        
        // Track outbound links
        document.querySelectorAll('a[href^="http"]').forEach(link => {
            link.addEventListener('click', function() {
                console.log(`🔗 Outbound link: ${this.href}`);
            });
        });
    },
    
    // Setup social share tracking
    setupShareTracking() {
        document.querySelectorAll('.share-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const platform = btn.classList[1];
                const title = document.querySelector('h1')?.textContent || document.title;
                this.data.socialShares[platform] = (this.data.socialShares[platform] || 0) + 1;
                this.saveData();
                trackShare(platform, title);
            });
        });
    },
    
    // Generate monitoring report
    generateReport() {
        const report = {
            timestamp: new Date().toISOString(),
            summary: {
                totalPageViews: Object.values(this.data.pageViews).reduce((a, b) => a + b, 0),
                totalArticles: Object.keys(this.data.articleReads).length,
                totalShares: Object.values(this.data.socialShares).reduce((a, b) => a + b, 0),
                totalProductClicks: Object.keys(this.data.productClicks).length
            },
            pageViews: this.data.pageViews,
            socialShares: this.data.socialShares,
            seoScores: {}
        };
        
        // Calculate SEO scores for each page
        Object.keys(this.data.pageViews).forEach(url => {
            report.seoScores[url] = this.updateSEOScore(url);
        });
        
        return report;
    },
    
    // Export report as JSON
    exportReport() {
        const report = this.generateReport();
        const blob = new Blob([JSON.stringify(report, null, 2)], {type: 'application/json'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `seo-report-${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
        console.log('📊 Report exported');
    },
    
    // Print report to console
    printReport() {
        const report = this.generateReport();
        console.log('=== SEO Monitoring Report ===');
        console.log(`Generated: ${report.timestamp}`);
        console.log(`\n📊 Summary:`);
        console.log(`  Total Page Views: ${report.summary.totalPageViews}`);
        console.log(`  Total Articles: ${report.summary.totalArticles}`);
        console.log(`  Total Shares: ${report.summary.totalShares}`);
        console.log(`  Product Clicks: ${report.summary.totalProductClicks}`);
        console.log('\n🏆 Top Pages by Views:');
        const sortedPages = Object.entries(report.pageViews)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 5);
        sortedPages.forEach(([url, views], i) => {
            console.log(`  ${i+1}. ${url}: ${views} views`);
        });
        console.log('\n📤 Share Breakdown:');
        Object.entries(report.socialShares).forEach(([platform, count]) => {
            console.log(`  ${platform}: ${count}`);
        });
        console.log('===========================');
    }
};

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize monitoring
    SEOMonitor.init();
    
    // Track article reads
    if (document.querySelector('article')) {
        const title = document.querySelector('article h1')?.textContent;
        if (title) {
            SEOMonitor.data.articleReads[title] = (SEOMonitor.data.articleReads[title] || 0) + 1;
            SEOMonitor.saveData();
            trackArticleView(title, 'Blog');
        }
    }
    
    // Track product clicks
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', function() {
            const productName = this.querySelector('h3')?.textContent;
            if (productName) {
                SEOMonitor.data.productClicks[productName] = (SEOMonitor.data.productClicks[productName] || 0) + 1;
                SEOMonitor.saveData();
                trackProductClick(productName);
            }
        });
    });
});

// Export functions globally for manual tracking
window.SEOMonitor = SEOMonitor;
window.trackShare = trackShare;
window.trackProductClick = trackProductClick;
window.trackArticleView = trackArticleView;
window.trackPageView = trackPageView;
window.initAnalytics = initAnalytics;
