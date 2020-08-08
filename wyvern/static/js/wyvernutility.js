$(document).ready(function(){
    /*
     * Confirm dialog 
     */
    $('.delete-confirm').on('click', function() {
        if (confirm("Are you sure?")) {
            return true;
        }
        return false;
    });

    /*
     * Slugify another field based on data target
     */
     
    $('.slugify').on('keyup', function() {
        var target = $(this).attr('data-target');
        $(target).val(slugify($(this).val()));
    });

    /* Hide Site Status, Site Owner, Site Type and Site Template if user is not WyvernAdmin */
    if(wyvernUser !== 'WyvernAdmin') {
      $("#div_id_site_owner, #div_id_site_type, #div_id_site_template, #div_id_site_status").hide();
    }

});

/* Slugify function */
function slugify(string) {
  const a = 'àáâäæãåāăąçćčđďèéêëēėęěğǵḧîïíīįìłḿñńǹňôöòóœøōõṕŕřßśšşșťțûüùúūǘůűųẃẍÿýžźż·/_,:;'
  const b = 'aaaaaaaaaacccddeeeeeeeegghiiiiiilmnnnnooooooooprrsssssttuuuuuuuuuwxyyzzz------'
  const p = new RegExp(a.split('').join('|'), 'g')

  var rand = function () {
    // Math.random should be unique because of its seeding algorithm.
    // Convert it to base 36 (numbers + letters), and grab the first 9 characters
    // after the decimal.
    return '-' + Math.random().toString(36).substr(2, 9);
  };

  console.log(rand());

  return string.toString().toLowerCase()
    .replace(/\s+/g, '-') // Replace spaces with -
    .replace(p, c => b.charAt(a.indexOf(c))) // Replace special characters
    .replace(/&/g, '-and-') // Replace & with 'and'
    .replace(/[^\w\-]+/g, '') // Remove all non-word characters
    .replace(/\-\-+/g, '-') // Replace multiple - with single -
    .replace(/^-+/, '') // Trim - from start of text
    .replace(/-+$/, '') // Trim - from end of text
    + rand()
}