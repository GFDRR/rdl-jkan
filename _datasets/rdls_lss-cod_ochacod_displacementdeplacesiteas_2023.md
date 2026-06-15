---
attributions:
- entity:
    affiliation: null
    email: null
    name: Commissions Mouvements de Populations (CMP)
    url: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM)
    url: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Democratic Republic of the Congo
    url: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
creator:
  affiliation: null
  email: null
  name: OCHA Democratic Republic of the Congo (DRC)
  url: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
dataset_id: rdls_lss-cod_ochacod_displacementdeplacesiteas_2023
description: "L'extrait de donn\xE9es mouvement de population (IDP) produit chaque\
  \ mois est fait suivant la m\xE9thodologie en vigueur en RDC . Pour avoir le nombre\
  \ de d\xE9plac\xE9s, elle recommande que soient consid\xE9r\xE9s les donn\xE9es\
  \ mouvements des d\xE9placements ayant \xE9t\xE9 \xE9valu\xE9es sur 2 ans en se\
  \ r\xE9f\xE9rant \xE0 la date d'\xE9valuation \xAB evaluation_date\xBB et ceci avec\
  \ comment r\xE9f\xE9rence le mois de l'extraction. Les colonnes \xAB person \xBB\
  \ et \xAB household \xBB reprennent respectivement le nombre des personnes et ceux\
  \ des m\xE9nages d\xE9plac\xE9s. Ces filtres sont applique sur la base de donn\xE9\
  es globale.. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly displacement data compiled from site assessments conducted
    by CMP, IOM, OCHA and partner organizations across DRC. Data includes household
    and person counts of internally displaced populations and returnees, tracked by
    administrative location, origin location, and displacement cause over a 2-year
    rolling evaluation window. Records are aggregated at health zone and site levels
    with temporal tracking via movement_date and evaluation_date fields.
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
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA Democratic Republic of the Congo
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/drc-displacement-deplace-site-assessment-ocha
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) and returnees from conflict and
      violence in DRC
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
  url: https://drive.google.com/file/d/1IgrUr-8s2-5SqVKl9Q1ThofGWRQ5m91R/view
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/17bbdeb9-5e54-4ae1-99a7-1cedcf2a2c8c/download/rdc_mouvement_de_population_deplace_stock_septembre_2025.xlsx
  format: null
  id: resource_17bbdeb9
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_stock_septembre_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Les donn\xE9es stock apr\xE8s la mise \xE0 jour d'ao\xFBt 2025)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/8c427095-5d54-4086-bf30-eb09a48ce812/download/rdc_mouvement_de_population_deplace_stock_aout_2025.xlsx
  format: null
  id: resource_8c427095
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_stock_aout_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/143a4a2d-e82d-43bb-a21b-92207a2b25c3/download/rdc_mouvement_de_population_deplace_stock_juillet_2025_update.xlsx
  format: null
  id: resource_143a4a2d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_stock_juillet_2025_update.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/069a2cdb-b577-4d17-80d8-747dae7a69ae/download/rdc_mouvement_de_population_deplace_mai_2025_maj.xlsx
  format: null
  id: resource_069a2cdb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mai_2025_maj.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/933ffaf5-05b5-4a95-9588-ed0ce2a55e11/download/rdc_mouvement_de_population_deplace_avril_2025.xlsx
  format: null
  id: resource_933ffaf5
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_avril_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data March 2025)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/2a122f7d-1555-48ea-8966-43af4447eaed/download/rdc_mouvement_de_population_deplace_mars_2025.xlsx
  format: null
  id: resource_2a122f7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mars_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data February 2025)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/442be6e6-9dc5-4a58-a1ef-8efb6177ab2e/download/rdc_mouvement_de_population_deplace_fev_2025.xlsx
  format: null
  id: resource_442be6e6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_fev_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data january 2025)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/770189a6-ac95-4f24-b6c0-b77f9f249563/download/rdc_mouvement_de_population_deplace_janvier_2025.xlsx
  format: null
  id: resource_770189a6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_janvier_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/8b99a144-b83d-4ed8-99cf-383c2c1435d6/download/rdc_mouvement_de_population_deplace_decembre_2024.xlsx
  format: null
  id: resource_8b99a144
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_d\xE9cembre_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/17820e6d-4ce1-4412-bce6-05d2e1b6f4b8/download/rdc_mouvement_de_population_deplace_novembre_2024.xlsx
  format: null
  id: resource_17820e6d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_novembre_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data Jul 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/b51d273a-61ec-48b7-8bfd-3fe1f6df1677/download/rdc_mouvement_de_population_deplace_juillet_2024.xlsx
  format: null
  id: resource_b51d273a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_juillet_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/a3c85764-a314-493f-be8d-38783c9ee7b3/download/rdc_mouvement_de_population_deplace_juin_2024.xlsx
  format: null
  id: resource_a3c85764
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_juin_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data May 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/c5faeab1-a08d-4a27-9043-2a3f58c4d461/download/rdc_mouvement_de_population_deplace_mai_2024.xlsx
  format: null
  id: resource_c5faeab1
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mai_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data April 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/1521e176-dc7d-42f6-a69e-f883c6e51f10/download/rdc_mouvement_de_population_deplace_avril_2024.xlsx
  format: null
  id: resource_1521e176
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rdc_mouvement_de_population_deplace_avril_2024.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data March 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/84b6fe99-9645-42eb-9b08-07239bfdd1b7/download/rdc_mouvement_de_population_deplace_mars_2024.xlsx
  format: null
  id: resource_84b6fe99
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_Mars_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data February 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/618daf61-db3e-4221-94f7-7b4e50accc06/download/rdc_mouvement_de_population_deplace_fev_2024.xlsx
  format: null
  id: resource_618daf61
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_fev_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data January 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/162ffb87-db78-4ed6-9a8d-64c0c69d81d8/download/rdc_mouvement_de_population_deplace_janvier_2024.xlsx
  format: null
  id: resource_162ffb87
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_janvier_2024.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data December 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/ed87cbc4-5eda-40e4-be70-6e9706ffcd4b/download/rdc_mouvement_de_population_deplace_decembre_2023.xlsx
  format: null
  id: resource_ed87cbc4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_d\xE9cembre_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data November 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/bf551725-25a7-4e21-9ece-4243d1e18069/download/rdc_mouvement_de_population_deplace_novembre_2023.xlsx
  format: null
  id: resource_bf551725
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_novembre_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data October 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/a90a4362-3c5a-4f21-ba3c-369fda5c61d5/download/rdc_mouvement_de_population_deplace_octobre_2023.xlsx
  format: null
  id: resource_a90a4362
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_octobre_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data September 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/be3575ad-3ff2-4aa5-93dc-dbc7cb86f211/download/rdc_mouvement_de_population_deplace_septembre_2023.xlsx
  format: null
  id: resource_be3575ad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_septembre_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data August 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/ec1bdccc-6b76-4323-b9cf-9232dd79e169/download/rdc_mouvement_de_population_deplace_aout_2023.xlsx
  format: null
  id: resource_ec1bdccc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_aout_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data July 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/ef8fc431-181c-40ef-9412-858dfb0d7417/download/rdc_mouvement_de_population_deplace_juillet_2023.xlsx
  format: null
  id: resource_ef8fc431
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_juillet_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data June 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/02e16333-11b6-4bd6-8569-fbb371fa9a08/download/rdc_mouvement_de_population_deplace_juin_2023.xlsx
  format: null
  id: resource_02e16333
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_juin_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data May 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/440bc879-bc54-41c9-b084-711a0d73f6f5/download/rdc_mouvement_de_population_deplace_mai_2023.xlsx
  format: null
  id: resource_440bc879
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mai_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data April 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/1f024a93-40bb-41ce-a6a7-2b196431113d/download/rdc_mouvement_de_population_deplace_avril_2023.xlsx
  format: null
  id: resource_1f024a93
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_avril_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data March 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/80a9fbac-e141-4765-84c3-fabf7414cf85/download/rdc_mouvement_de_population_deplace_mars_2023.xlsx
  format: null
  id: resource_80a9fbac
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mars_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data February 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/89ba7dfb-194c-4cf8-bcee-828b9d82fb27/download/rdc_mouvement_de_population_deplace_fevrier_2023.xlsx
  format: null
  id: resource_89ba7dfb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_fevrier_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data January 2023)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/5269d775-a68f-44f0-b8c7-97063da9942c/download/rdc_mouvement_de_population_deplace_janvier_2023.xlsx
  format: null
  id: resource_5269d775
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_janvier_2023.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data December 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/6bc6c3fe-a699-45ff-bfb8-7edc5024f92a/download/rdc_mouvement_de_population_deplacee_decembre_2022-.xlsx
  format: null
  id: resource_6bc6c3fe
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_decembre_2022--.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data November 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/10869ae8-a33c-487e-8160-e1da31d39f68/download/rdc_mouvement_de_population_deplacee_novembre_2022.xlsx
  format: null
  id: resource_10869ae8
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_novembre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data October 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/998836a4-0738-47d4-896b-1b8f5ea31c77/download/rdc_mouvement_de_population_deplacee_octobre_2022.xlsx
  format: null
  id: resource_998836a4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_octobre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data September 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/31d6dcaf-cccb-4cf1-9a25-88040b0ba1fe/download/rdc_mouvement_de_population_deplacee_septembre_2022.xlsx
  format: null
  id: resource_31d6dcaf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_septembre_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data Aout 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/2382328d-5da8-49e7-a7ef-e27db4e443d8/download/rdc_mouvement_de_population_deplacee_aout_2022.xlsx
  format: null
  id: resource_2382328d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplacee_Ao\xFBt_2022.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data July 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/32bf635f-6620-43f4-819c-e820309e7deb/download/rdc_mouvement_de_population_deplacee_juillet_2022.xlsx
  format: null
  id: resource_32bf635f
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_juillet_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data June 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/0e2be415-74b0-482b-826a-f4b338fdc86c/download/rdc_mouvement_de_population_deplacee_juin_2022.xlsx
  format: null
  id: resource_0e2be415
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_juin_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data May 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/ada00afa-80b6-43bf-a039-c9c785544686/download/rdc_mouvement_de_population_deplacee_mai_2022.xlsx
  format: null
  id: resource_ada00afa
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_mai_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data April 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/05d9d81e-ad3f-4d06-981c-4c9c3ad17984/download/rdc_mouvement_de_population_deplacee_avril_2022.xlsx
  format: null
  id: resource_05d9d81e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_Avril_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data March 2022)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/f145766b-8abf-42e3-ba14-3c986b2540ce/download/rdc_mouvement_de_population_deplacee_mars_2022.xlsx
  format: null
  id: resource_f145766b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: RDC_mouvement_de_population_deplacee_Mars_2022.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data November 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/ee28d4de-3438-4213-bff5-7c28a9ec5c91/download/rdc_mouvement_de_population_deplace_novembre_2021.xlsx
  format: null
  id: resource_ee28d4de
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Novembre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data October 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/2d81048d-5b77-4960-8190-e518bfdf7db3/download/rdc_mouvement_de_population_deplace_octobre_2021.xlsx
  format: null
  id: resource_2d81048d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Octobre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data September 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/d885a4cb-4e71-43e5-a35e-2e052529be11/download/rdc_mouvement_de_population_deplace_septembre_2021.xlsx
  format: null
  id: resource_d885a4cb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Septembre_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data Aout 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/c540cb68-440a-4046-b503-d653698b2742/download/rdc_mouvement_de_population_deplace_aout_2021.xlsx
  format: null
  id: resource_c540cb68
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Ao\xFBt_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data July 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/c74e947d-1d0e-4fd0-8cb6-56b9bd703b9c/download/rdc_mouvement_de_population_deplace_juillet_2021.xlsx
  format: null
  id: resource_c74e947d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Juillet_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (Excel)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/fe6ac3c7-aa7c-4271-a787-cd2cf189831a/download/rdc_mouvement_de_population_deplace_avril_2025.xlsx
  format: null
  id: resource_fe6ac3c7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_avril_2025.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data june 2021)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/8b9d2e6e-81be-4550-b416-bab7282d2f4a/download/rdc_mouvement_de_population_deplace_juin_2021.xlsx
  format: null
  id: resource_8b9d2e6e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_deplac\xE9_Juin_2021.xlsx"
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] -\
    \ Site Assessment (DRC IDPs data May 2024)"
  download_url: https://data.humdata.org/dataset/6e2f67e6-f9af-4e99-b548-80202a0aa5a2/resource/e29c46db-97cf-4cb1-82a8-9cc062ec0ab1/download/rdc_mouvement_de_population_deplace_mai_2024.xlsx
  format: null
  id: resource_e29c46db
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "RDC_mouvement_de_population_d\xE9plac\xE9_mai_2024.xlsx"
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-cod_ochacod_displacementdeplacesiteas_2023
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
  start: '2023-06-01'
temporal_resolution: null
title: "Democratic Republic of the Congo: Displacement - [D\xE9plac\xE9] - Site Assessment"
version: null
vulnerability: null
---
