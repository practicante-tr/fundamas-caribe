$(document).ready(function() {

    (function($) {
        "use strict";


        jQuery.validator.addMethod('answercheck', function(value, element) {
            return this.optional(element) || /^\bcat\b$/.test(value)
        }, "type the correct answer -_-");

        // validate contactForm form
        $(function() {
            $('#contactForm').validate({
                rules: {
                    name: {
                        required: true,
                        minlength: 2
                    },
                    subject: {
                        required: true,
                        minlength: 4
                    },
                    number: {
                        required: true,
                        minlength: 5
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    message: {
                        required: true,
                        minlength: 20
                    }
                },
                messages: {
                    name: {
                        required: "vamos, debes tener un nombre, no?",
                        minlength: "su nombre debe tener al menos 2 caracteres"
                    },
                    subject: {
                        required: "perdonanos, pero debes darle un titulo a esta comunicación",
                        minlength: "su nombre debe tener al menos 4 caracteres"
                    },
                    number: {
                        required: "come on, you have a number, don't you?",
                        minlength: "su nombre debe tener al menos 5 caracteres"
                    },
                    email: {
                        required: "sin email? la idea es entregarte respuesta a tu consulta, no lo crees?"
                    },
                    message: {
                        required: "tienes que escribir algo para enviar este formulario.",
                        minlength: "seguro que es todo lo que quieres?"
                    }
                },
                // submitHandler: function(form) {
                //     $(form).ajaxSubmit({
                //         type:"POST",
                //         data: $(form).serialize(),
                //         url:"contact_process.php",
                //         success: function() {
                //             $('#contactForm :input').attr('disabled', 'disabled');
                //             $('#contactForm').fadeTo( "slow", 1, function() {
                //                 $(this).find(':input').attr('disabled', 'disabled');
                //                 $(this).find('label').css('cursor','default');
                //                 $('#success').fadeIn()
                //                 $('.modal').modal('hide');
                //             	$('#success').modal('show');
                //             })
                //         },
                //         error: function() {
                //             $('#contactForm').fadeTo( "slow", 1, function() {
                //                 $('#error').fadeIn()
                //                 $('.modal').modal('hide');
                //             	$('#error').modal('show');
                //             })
                //         }
                //     })
                // }
            })
        })

    })(jQuery)
})