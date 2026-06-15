---
attributions:
- entity:
    affiliation: null
    email: null
    name: Commissions Mouvements de Populations (CMP)
    url: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OIM (International Organization for Migration)
    url: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA (UN Office for the Coordination of Humanitarian Affairs)
    url: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
dataset_id: rdls_lss-cod_ochacod_displacementreturneessite_2022
description: "L'extrait de donn\xE9es mouvement de population (Retour) produit chaque\
  \ mois est fait suivant la m\xE9thodologie en vigueur en RDC . Pour avoir le nombre\
  \ des retourn\xE9es, elle recommande que soient consid\xE9r\xE9s les donn\xE9es\
  \ mouvements retour ayant \xE9t\xE9 \xE9valu\xE9es sur 2 ans en se r\xE9f\xE9rant\
  \ \xE0 la date d'\xE9valuation \xAB evaluation_date\xBB et ceci avec comme r\xE9\
  f\xE9rence le mois de l'extraction mais \xE9galement, en prenant unique les mouvements\
  \ ayant enregistr\xE9s les 18 derniers mois en se basant sur la date mouvement \xAB\
  \ movement_date \xBB . Les colonnes \xAB person \xBB et \xAB household \xBB reprennent\
  \ respectivement le nombre des personnes et ceux des m\xE9nages d\xE9plac\xE9s.\
  \ Ces filtres sont applique sur la base de donn\xE9es globale.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly population movement data (returnees) collected through site
    assessments by CMP, OIM, OCHA and partners following DRC methodology. Data aggregates
    return movements evaluated over 2-year rolling windows with reference to evaluation_date
    and movement_date, compiled into monthly stock reports at health zone and administrative
    division levels.
  sources:
  - id: source_1
    license: null
    name: Commissions Mouvements de Populations (CMP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OIM (International Organization for Migration)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA (UN Office for the Coordination of Humanitarian Affairs)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/drc-displacement-idps-site-assessment-ocha
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement and return movements tracked by site assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://drive.google.com/file/d/1IgrUr-8s2-5SqVKl9Q1ThofGWRQ5m91R/view?usp=sharing
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/7077a74c-9800-435d-bb58-8059eb36e43f/download/rdc_mouvement_de_population_retourne_stock_septembre_2025.xlsx
  format: null
  id: resource_7077a74c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9_stock_septembre_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [returnees] - Site\
    \ Assessment (Les donn\xE9es du stcok apr\xE8s la mise \xE0 jour d'ao\xFBt 2025)"
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/d8116e7f-bf40-4316-9b31-2106c4832c92/download/rdc_mouvement_de_population_retourne_stock_aout_2025.xlsx
  format: null
  id: resource_d8116e7f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_stock_aout_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/5db48266-4eed-45c1-bc65-1900fcaf61ad/download/rdc_mouvement_de_population_retourne_mai_2025.xlsx
  format: null
  id: resource_5db48266
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc_mouvement_de_population_retourne_mai_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/301fc41e-9811-4c3d-bd7d-0dd9031b6a23/download/rdc_mouvement_de_population_retourne_stock_juillet_2025_update.xlsx
  format: null
  id: resource_301fc41e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_stock_juillet_2025_update.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/c5a1db97-c99f-47ef-a4e2-90f3d3a76c8f/download/rdc_mouvement_de_population_retourne_avril_2025.xlsx
  format: null
  id: resource_c5a1db97
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_avril_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b27d567d-97a8-43b3-95bf-01e7494cab48/download/rdc_mouvement_de_population_retourne_mars_2025.xlsx
  format: null
  id: resource_b27d567d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_mars_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b1473139-c713-450e-a203-681927f1eafb/download/rdc_mouvement_de_population_retourne_fev_2025.xlsx
  format: null
  id: resource_b1473139
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_fev_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/198986f8-63de-47ee-af00-c844143f5e9e/download/rdc_mouvement_de_population_retourne_janvier_2025.xlsx
  format: null
  id: resource_198986f8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retourne_janvier_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/7b328638-cb69-41a2-a13e-44c0481e8ccd/download/rdc_mouvement_de_population_retournee_decembre_2024.xlsx
  format: null
  id: resource_7b328638
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retournee_d\xE9cembre_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/be608b1e-c45a-4a97-b9a3-5cda5438aebd/download/rdc_mouvement_de_population_retournee_novembre_2024.xlsx
  format: null
  id: resource_be608b1e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_novembre_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Jul 2024)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/a6ad3361-1790-4775-8de4-1fd8b87a1109/download/rdc_mouvement_de_population_retournee_juillet_2024.xlsx
  format: null
  id: resource_a6ad3361
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_juillet_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (Excel)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/29f31695-4107-4541-a510-18e3ac7e9727/download/rdc_mouvement_de_population_retournees_juin_2024.xlsx
  format: null
  id: resource_29f31695
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9es_juin_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Apr 2024)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/a9218df5-a92a-4abd-ad87-99a19db2d9c4/download/rdc_mouvement_de_population_retournee_avril_2024.xlsx
  format: null
  id: resource_a9218df5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_avril_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Mar 2024)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/adccd7eb-7c79-4023-875e-857ccd8b21b7/download/rdc_mouvement_de_population_retournee_mars_2024.xlsx
  format: null
  id: resource_adccd7eb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_Mars_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Feb 2024)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b4e4d100-53c5-40b3-9296-d1b4de2545da/download/rdc_mouvement_de_population_retournee_ferv_2024.xlsx
  format: null
  id: resource_b4e4d100
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_fev_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Jan 2024)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/a757f902-3083-42a2-a2f3-cfc616b70e2f/download/rdc_mouvement_de_population_retournee_janvier_2024.xlsx
  format: null
  id: resource_a757f902
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_janvier_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Dec 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/1d9db370-fd88-4844-8caf-a3871ca4fba8/download/rdc_mouvement_de_population_retournee_decembre_2023.xlsx
  format: null
  id: resource_1d9db370
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retournee_d\xE9cembre_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Nov 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/bde430bc-85e0-4af7-b644-409b063639e6/download/rdc_mouvement_de_population_retournee_novembre_2023.xlsx
  format: null
  id: resource_bde430bc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_novembre_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Oct 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/992aebd6-19e4-45f1-add9-7f92fa260b9b/download/rdc_mouvement_de_population_retournee_octobre_2023.xlsx
  format: null
  id: resource_992aebd6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_octobre_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data sep 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b96df92b-f2d5-478c-8a11-72268e774220/download/rdc_mouvement_de_population_retournee_septembre_2023.xlsx
  format: null
  id: resource_b96df92b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_septembre_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Aug 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/6fd51c74-f391-4e14-adc1-c1f9cb01d922/download/rdc_mouvement_de_population_retournee_aout_2023.xlsx
  format: null
  id: resource_6fd51c74
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_aout_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Jul 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/d6d5a9fa-b5b8-4747-98f7-8ffa4573c63f/download/rdc_mouvement_de_population_retournee_juillet_2023.xlsx
  format: null
  id: resource_d6d5a9fa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_juillet_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data jun 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/991081f4-acc3-4827-b06a-e6af921ba2f5/download/rdc_mouvement_de_population_retournee_juin_2023.xlsx
  format: null
  id: resource_991081f4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_juin_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data May 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/06219f1d-1914-4602-80cf-fecb8200ebb2/download/rdc_mouvement_de_population_retournee_mai_2023.xlsx
  format: null
  id: resource_06219f1d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_mai_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Apr 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/17af84a0-a2ab-451d-bae9-948a44d2cecf/download/rdc_mouvement_de_population_retournee_avril_2023.xlsx
  format: null
  id: resource_17af84a0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_avril_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Mar 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/bf3ef6d9-8eae-4fd1-a34d-4bf90cd0bea6/download/rdc_mouvement_de_population_retournee_mars_2023.xlsx
  format: null
  id: resource_bf3ef6d9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_mars_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Feb 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/f63cc5e2-2b86-4dea-a7b9-1e209c96c014/download/rdc_mouvement_de_population_retournee_fevrier_2023.xlsx
  format: null
  id: resource_f63cc5e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_fevrier_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Jan 2023)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/7a84f668-79f1-41ab-b3fa-711b3ef98c57/download/rdc_mouvement_de_population_retournee_janvier_2023.xlsx
  format: null
  id: resource_7a84f668
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_janvier_2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Dec 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/5dd5c08e-7edb-4425-8d59-01bf47de1d59/download/rdc_mouvement_de_population_retournee_decembre_2022-.xlsx
  format: null
  id: resource_5dd5c08e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retournee_d\xE9cembre_2022--.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Nov 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/910e8379-9333-4b9b-bcf7-021f0442139a/download/rdc_mouvement_de_population_retournee_novembre_2022.xlsx
  format: null
  id: resource_910e8379
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_novembre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data October 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/08f2d6c2-13fa-4652-a3a8-8a4dbac00046/download/rdc_mouvement_de_population_retournee_octobre_2022.xlsx
  format: null
  id: resource_08f2d6c2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_octobre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data September 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/d9c98ffb-b780-4839-beb1-fb09345dacff/download/rdc_mouvement_de_population_retournee_septembre_2022.xlsx
  format: null
  id: resource_d9c98ffb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_septembre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Aout 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/5f17d3d5-5fc4-451f-aab1-a8cd2f7fa95c/download/rdc_mouvement_de_population_retournee_aout_2022.xlsx
  format: null
  id: resource_5f17d3d5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retournee_ao\xFBt_2022.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data July 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/4f6d420d-8af1-4b77-9960-a4b9d94f783f/download/rdc_mouvement_de_population_retournee_juillet_2022.xlsx
  format: null
  id: resource_4f6d420d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_juillet_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data June 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/4b3b9db5-64f8-4965-a37e-a514fe6c0724/download/rdc_mouvement_de_population_retournee_juin_2022.xlsx
  format: null
  id: resource_4b3b9db5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_juin_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data May 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/1c2a72d0-07e1-4d09-8fda-79949756a8bc/download/rdc_mouvement_de_population_retournee_mai_2022.xlsx
  format: null
  id: resource_1c2a72d0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_mai_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data April 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/871021f8-9c57-4cad-958a-babf01f42cbc/download/rdc_mouvement_de_population_retournee_avril_2022.xlsx
  format: null
  id: resource_871021f8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_Avril_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data March 2022)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b9145092-7d09-49a6-beee-ea4fc4189b87/download/rdc_mouvement_de_population_retournee_mars_2022.xlsx
  format: null
  id: resource_b9145092
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_retournee_Mars_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data November 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/e5d038db-a824-4bf6-99cd-fd9f88c79fe9/download/rdc_mouvement_de_population_retourne_novembre_2021.xlsx
  format: null
  id: resource_e5d038db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9_Novembre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data October 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/cd503075-3f3d-48b5-ab08-b39a1b0e5bad/download/rdc_mouvement_de_population_retourne_octobre_2021.xlsx
  format: null
  id: resource_cd503075
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9_Octobre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data September 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/43920de4-fbc5-4b8e-a64d-10fa89befe78/download/rdc_mouvement_de_population_retourne_septembre_2021.xlsx
  format: null
  id: resource_43920de4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9_Septembre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data Aout 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/daa1b085-250d-457b-8863-56a6e3d58748/download/rdc_mouvement_de_population_retour_aout_2021.xlsx
  format: null
  id: resource_daa1b085
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_Retour_Ao\xFBt_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data July 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/b5570eae-f2ea-4726-9833-8ec5288944d9/download/rdc_mouvement_de_population_retour_juillet_2021.xlsx
  format: null
  id: resource_b5570eae
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_Retour_Juillet_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data June 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/f2df55d9-7be8-4ffa-96d0-6ff63b94718e/download/rdc_mouvement_de_population_retourne_juin_2021.xlsx
  format: null
  id: resource_f2df55d9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_retourn\xE9_Juin_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data February 2021)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/6feb0810-c70f-4615-b289-383e502b9941/download/20200304_v100_mouvement_de_population_filtered.xlsx
  format: null
  id: resource_6feb0810
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_fev_2020.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic Republic of the Congo: Displacement - [returnees] - Site
    Assessment (DRC Returnees data December 2019)'
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/50851b38-0f1c-4320-9216-2acab748f3c0/download/20191231_v100_mouvement_de_population_2019-validated.xlsx
  format: null
  id: resource_50851b38
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9c-2019 - VALIDATED.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [returnees] - Site\
    \ Assessment (R\xE9sum\xE9 methodologie.docx)"
  download_url: https://data.humdata.org/dataset/87e078ae-98bd-44a9-93bb-517dea483f84/resource/96b0ce8c-5d4f-4069-be11-247d6f316d4c/download/resume-methodologie.docx
  format: DOCX
  id: resource_96b0ce8c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "R\xE9sum\xE9 methodologie.docx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_displacementreturneessite_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-09-30'
  start: '2022-12-01'
temporal_resolution: null
title: 'Democratic Republic of the Congo: Displacement - [returnees] - Site Assessment'
version: null
vulnerability: null
---
