---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNICEF
    url: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: FSNAU (Food Security and Nutrition Analysis Unit)
    url: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence
creator:
  affiliation: null
  email: null
  name: OCHA Somalia
  url: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence
dataset_id: rdls_lss-som_ochasom_acutemalnutrition_2022
description: 'Global Acute Malnutrition (GAM) is the presence of both moderate acute
  malnutrition (MAM) and severe acute malnutrition (SAM) in a population. Height and
  body weight ratios are measured for children between 6 months and 5 years old to
  determine the prevalence of malnutrition. Rates above 15 per cent are ordinarily
  considered an emergency but rates above 30 per cent contribute to the case for famine
  in a given area.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Height and body weight measurements for children aged 6-59 months were
    collected through FSNAU nutrition surveys across Somalia districts during post-Gu
    seasons (2017-2023). Survey data were analyzed to calculate prevalence rates of
    Severe Acute Malnutrition (SAM), Moderate Acute Malnutrition (MAM), and Global
    Acute Malnutrition (GAM), with results classified using IPC AMN standards to assess
    nutrition emergency severity by district.
  sources:
  - id: source_1
    license: null
    name: UNICEF
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: FSNAU (Food Security and Nutrition Analysis Unit)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/somalia-acute-malnutrition-burden-and-prevalence
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Acute malnutrition prevalence in children aged 6-59 months as a direct
      impact of food insecurity and drought conditions
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
  url: https://www.fsnau.org/analytical-approach/methodology/nutrition
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Acute Malnutrition (Excel)'
  download_url: https://data.humdata.org/dataset/6c4c69cf-8ca0-4bfc-8c46-73cdb18812d5/resource/b9718d0d-4c2f-48ee-a283-350b97e892c5/download/somalia-2023-post-gu-acute-malnutrition-burden-and-prevalence-by-district-21-sep-2023-1.xlsx
  format: null
  id: resource_b9718d0d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: somalia-2023-post-gu-acute-malnutrition-burden-and-prevalence-by-district-21-sep-2023.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia 2022 Post Gu Total Acute Malnutrition Burden and Prevalence
    for Aug 2022 to Jul 2023 by District .xlsx
  download_url: https://data.humdata.org/dataset/6c4c69cf-8ca0-4bfc-8c46-73cdb18812d5/resource/cfe1321e-89ce-43f3-b067-6da4bbb3ca80/download/somalia-2022-post-gu-total-acute-malnutrition-burden-and-prevalence-for-aug-2022-to-jul-2023-by.xlsx
  format: null
  id: resource_cfe1321e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Somalia 2022 Post Gu Total Acute Malnutrition Burden and Prevalence for Aug
    2022 to Jul 2023 by District .xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Acute Malnutrition (2021 Post Gu AMN Burden and Prevalence
    - 9 Sep 2021)'
  download_url: https://data.humdata.org/dataset/6c4c69cf-8ca0-4bfc-8c46-73cdb18812d5/resource/d52e624e-87c8-40cd-bf82-27d37da0fb93/download/2021-post-gu-amn-burden-and-prevalence-9-sep-2021.xlsx
  format: null
  id: resource_d52e624e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 2021 Post Gu AMN Burden and Prevalence - 9 Sep 2021
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Acute Malnutrition (FSNAU Nutrition Surveys data-Gu and
    Deyr 2020)'
  download_url: https://data.humdata.org/dataset/6c4c69cf-8ca0-4bfc-8c46-73cdb18812d5/resource/3adcf96d-0e38-4f3b-8fb6-20a6fd6c9a25/download/fsnau-nutrition-surveys-data-gu-and-deyr-2020.xlsx
  format: null
  id: resource_3adcf96d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSNAU Nutrition Surveys data-Gu and Deyr 2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Somalia : Acute Malnutrition (FSNAU Survey Results- 2017-2020)'
  download_url: https://data.humdata.org/dataset/6c4c69cf-8ca0-4bfc-8c46-73cdb18812d5/resource/db721063-7eac-4a3c-ab48-b629f7554d84/download/fsnau-survey-results-2017-2020.xlsx
  format: null
  id: resource_db721063
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FSNAU Survey Results- 2017-2020
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-som_ochasom_acutemalnutrition_2022
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-09-21'
  start: '2022-08-01'
temporal_resolution: null
title: 'Somalia : Acute Malnutrition'
version: null
vulnerability: null
---
