// frappe.ui.form.on('Library Transaction', {
//     refresh: function(frm) {
//         let custom_button = frm.add_custom_button('Has Fine?', () => {
//             console.log("Button clicked"); // Debugging statement
//             show_pending_fine_notification(frm);
//         });
//
//         custom_button.css({
//             'background-color': '#ff6347', // Tomato color
//             'color': '#fff' // White text color
//         });
//
//         // Set query for article field to only show available articles in child table
//         frm.fields_dict.items.grid.get_field('article').get_query = function() {
//             return {
//                 filters: {
//                     status: 'Available'
//                 }
//             };
//         };
//     }
// });
//
// function show_pending_fine_notification(frm) {
//     let d = new frappe.ui.Dialog({
//         title: 'Pending Fine',
//         fields: [{
//             fieldtype: 'HTML',
//             options: '<p>You have a pending fine to pay.</p>'
//         }],
//         primary_action_label: 'Proceed',
//         primary_action(values) {
//             console.log("Proceed button clicked"); // Debugging statement
//             d.hide(); // Hide the dialog
//             show_fine_details_dialog(frm);
//         }
//     });
//
//     d.show();
// }
//
// function show_fine_details_dialog(frm) {
//     let d = new frappe.ui.Dialog({
//         title: 'Enter details',
//         fields: [{
//                 label: 'Date of Transaction',
//                 fieldname: 'date',
//                 fieldtype: 'Date'
//             },
//             {
//                 label: 'Total fine',
//                 fieldname: 'total_fine',
//                 fieldtype: 'Currency'
//             }
//         ],
//         primary_action_label: 'Submit',
//         primary_action(values) {
//             console.log(values);
//             // Perform any necessary action here (e.g., save data to server)
//             d.hide();
//         }
//     });
//
//     d.show();
// }



frappe.ui.form.on('Library Transaction', {
    refresh: function(frm) {
        let custom_button = frm.add_custom_button('Has Fine?', () => {
            console.log("Button clicked"); // Debugging statement
            show_pending_fine_notification(frm);
        });

        custom_button.css({
            'background-color': '#ff6347', // Tomato color
            'color': '#fff' // White text color
        });

        // Set query for article field to only show available articles
        frm.set_query('article', () => {
            return {
                filters: {
                    status: 'Available'
                }
            };
        });
    }
});

function show_pending_fine_notification(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Pending Fine',
        fields: [{
            fieldtype: 'HTML',
            options: '<p>You have a pending fine to pay.</p>'
        }],
        primary_action_label: 'Proceed',
        primary_action(values) {
            console.log("Proceed button clicked"); // Debugging statement
            d.hide(); // Hide the dialog
            show_fine_details_dialog(frm);
        }
    });

    d.show();
}

function show_fine_details_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Enter details',
        fields: [{
                label: 'Date of Transaction',
                fieldname: 'date',
                fieldtype: 'Date'
            },
            {
                label: 'Total fine',
                fieldname: 'total_fine',
                fieldtype: 'Currency'
            }
        ],
        primary_action_label: 'Submit',
        primary_action(values) {
            console.log(values);
            // Perform any necessary action here (e.g., save data to server)
            d.hide();
        }
    });

    d.show();
}
