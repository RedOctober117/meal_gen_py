SELECT 
  *
FROM
  servings
    JOIN (SELECT * FROM meal_compositions GROUP BY meal_id) meal_composition_view USING(serv_id);

SELECT meal_names.meal_id, meal_names.meal_name, SUM(servings.serv_cal), SUM(servings.serv_fat_tot), SUM(servings.serv_fat_sat), SUM(servings.serv_fat_trans), SUM(servings.serv_chol), SUM(servings.serv_sod), SUM(servings.serv_carb_tot), SUM(servings.serv_fiber_diet), SUM(servings.serv_sugar_tot), SUM(servings.serv_sugar_add), SUM(servings.serv_prot), SUM(servings.serv_vit_d), SUM(servings.serv_calcium), SUM(servings.serv_iron), SUM(servings.serv_potas) FROM servings JOIN meal_compositions USING(serv_id) JOIN meal_names USING(meal_id) GROUP BY meal_id;
