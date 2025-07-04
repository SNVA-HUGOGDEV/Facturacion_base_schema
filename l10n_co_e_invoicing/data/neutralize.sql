-- Poner en modo pruebas
UPDATE res_company
SET profile_execution_id = '2',
test_set_id = '0000005', 
software_id = '0000005',
software_pin = '0000005';

-- Desactivar crons
UPDATE ir_cron
   SET active = false
 WHERE id IN (
       SELECT res_id
         FROM ir_model_data
        WHERE model = 'ir.cron'
          AND name = 'ir_cron_auto_post_dian_entry'
          AND module = 'l10n_co_e_invoicing'
);
