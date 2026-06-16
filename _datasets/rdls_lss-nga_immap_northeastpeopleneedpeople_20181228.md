---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Needs Overview for the Nutrition Sector
    url: https://data.humdata.org/dataset/north-east-nigeria-people-in-need-and-people-targeted-for-nutrition-assistance-in-2019
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/north-east-nigeria-people-in-need-and-people-targeted-for-nutrition-assistance-in-2019
creator:
  affiliation: null
  email: null
  name: iMMAP Inc.
  url: https://data.humdata.org/dataset/north-east-nigeria-people-in-need-and-people-targeted-for-nutrition-assistance-in-2019
dataset_id: rdls_lss-nga_immap_northeastpeopleneedpeople_20181228
description: 'The zipped CSV file details the estimated people in need and people
  targeted for nutrition support at the Local Government Authority (LGA) level in
  all three crisis-affected states of north east Nigeria. Among other elements, it
  presents the breakdown people in need and people targeted, by settlement type (notably
  in Internally Displaced Persons (IDP) Camps, Host Communities and in Inaccessible
  Areas).. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/north-east-nigeria-people-in-need-and-people-targeted-for-nutrition-assistance-in-2019]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Humanitarian Needs Overview data for the nutrition sector in north
    east Nigeria was compiled at the Local Government Authority level, disaggregating
    people in need and people targeted for nutrition support by settlement type (IDP
    camps, host communities, inaccessible areas) to inform the 2019 Humanitarian Response
    Plan.
  sources:
  - id: source_1
    license: null
    name: Humanitarian Needs Overview for the Nutrition Sector
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/north-east-nigeria-people-in-need-and-people-targeted-for-nutrition-assistance-in-2019
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need of nutrition assistance due to drought-driven food
      insecurity in north east Nigeria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People targeted for nutrition support interventions in north east
      Nigeria
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The zipped CSV file details the estimated people in need and people
    targeted for nutrition support at the Local Government Authority (LGA) level in
    all three crisis-affected states of north east Nigeria.
  download_url: https://data.humdata.org/dataset/c1280391-c1f8-4f38-9b24-9621433c9959/resource/73b6a098-9f28-4116-a91a-04f97f0d2db5/download/nga_ne_nigeria_nutrition_sector_people_in_need_and_people_targeted_for_support_in_2019.zip
  format: null
  id: resource_73b6a098
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_NE_Nigeria_Nutrition_Sector_People_in_Need_and_People_Targeted_for_Support_in_2019.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-nga_immap_northeastpeopleneedpeople_20181228
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-12-28'
temporal_resolution: null
title: North East Nigeria People in Need and People Targeted for Nutrition Assistance
  in 2019.
version: null
vulnerability: null
---
