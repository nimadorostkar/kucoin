/**
 * Perfect Scrollbar
 */
'use strict';

document.addEventListener('DOMContentLoaded', function () {
  (function () {
    const verticalExample = document.getElementById('vertical-example'),
      verticalDepth = document.getElementById('vertical-depth'),
      horizontalExample = document.getElementById('horizontal-example'),
      verticalKlines = document.getElementById('vertical-klines'),
      verticalMarkets = document.getElementById('vertical-markets'),
      horizVertExample = document.getElementById('both-scrollbars-example');



    // Vertical Example
    // --------------------------------------------------------------------
    if (verticalExample) {
      new PerfectScrollbar(verticalExample, {
        wheelPropagation: false
      });
    }


    // Vertical Example
    // --------------------------------------------------------------------
    if (verticalDepth) {
      new PerfectScrollbar(verticalDepth, {
        wheelPropagation: false
      });
    }

    // Horizontal Example
    // --------------------------------------------------------------------
    if (horizontalExample) {
      new PerfectScrollbar(horizontalExample, {
        wheelPropagation: false,
        suppressScrollY: true
      });
    }


    // Vertical Example
    // --------------------------------------------------------------------
    if (verticalKlines) {
      new PerfectScrollbar(verticalKlines, {
        wheelPropagation: false
      });
    }



    // Vertical Example
    // --------------------------------------------------------------------
    if (verticalMarkets) {
      new PerfectScrollbar(verticalMarkets, {
        wheelPropagation: false
      });
    }




    // Both vertical and Horizontal Example
    // --------------------------------------------------------------------
    if (horizVertExample) {
      new PerfectScrollbar(horizVertExample, {
        wheelPropagation: false
      });
    }
  })();
});
