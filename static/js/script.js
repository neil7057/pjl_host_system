// select 2 for multiselect - select2.org/getting-started/basic-usage
// Initialize select2

$(document).ready(function () {
    $('#thread_tags').select2({
      placeholder: "Select Tags",
      tags: true,
      tokenSeparators: [',', ' '],
      // apply selection limit with Select2 (https://select2.org/selections)
      maximumSelectionLength: 4,
    });
  });
