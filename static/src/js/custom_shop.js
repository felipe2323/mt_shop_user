odoo.define('mt_shop_user.custom_shop', (require) => {

    const { Widget, registry} = require('web.public.widget');
    const WidgetCustomShopHide = Widget.extend({
        selector: '.js_custom_shop',
        events: {
            'click .field-has_shop': 'clickEventHasShop',
        },
        start () {
            this._super(...arguments);
            this.$('.field-shop_name').hide();
            this.$('.field-shop_description').hide();
        },
        clickEventHasShop (ev){
            if ($(ev.target).is("input") &&
                $(ev.target).val() == 'on'){
                this.$('.field-shop_name').toggle();
                this.$('.field-shop_description').toggle();
            }

        },
    });
    registry.WidgetCustomShopHide = WidgetCustomShopHide;

});