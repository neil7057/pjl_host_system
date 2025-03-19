// select 2 for multiselect - select2.org/getting-started/basic-usage
// Initialize select2

// $(document).ready(function() {
//   $('#id_categories').select2();
// });

$(document).ready(function () {
  $('#id_categories').select2({
    placeholder: "Select Category",
    tags: true,
    tokenSeparators: [',', ' '],
  });
});
