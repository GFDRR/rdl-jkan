---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    url: https://data.humdata.org/dataset/afghanistan-displacement-data-climate-vulnerability-assessment-iom-dtm
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/afghanistan-displacement-data-climate-vulnerability-assessment-iom-dtm
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/afghanistan-displacement-data-climate-vulnerability-assessment-iom-dtm
dataset_id: rdls_lss-afg_iom_displacementdataclimatevu_2024
description: 'Afghanistan has experienced intensifying drought, severe floods and
  extreme weather conditions amid the aggravation of the global climate crisis. IOM
  has initiated the Afghanistan Climate Vulnerability Assessment Programme (ACVA)
  - a nationwide community-level assessment programme designed in coordination with
  the de-facto Afghanistan National Disaster Management Authority (ANDMA) to evaluate
  the effects and risks of climate change and disasters on Afghan people.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/afghanistan-displacement-data-climate-vulnerability-assessment-iom-dtm]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: IOM conducted a nationwide community-level assessment programme (ACVA)
    in coordination with Afghanistan's National Disaster Management Authority to evaluate
    climate change and disaster impacts on Afghan populations. Data was collected
    through DTM standard methodology across two rounds (January 2025 and May 2025),
    capturing household and individual displacement flows by province and district
    in response to drought, floods, and extreme weather conditions.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM) Displacement Tracking Matrix
      (DTM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/afghanistan-displacement-data-climate-vulnerability-assessment-iom-dtm
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons arriving in communities due to drought
      and climate-related hazards
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
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons arriving in communities due to severe
      floods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
  - asset_category: population
    asset_dimension: population
    description: Returnees to communities from internal and external displacement
      due to drought and climate vulnerability
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_3
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
  - asset_category: population
    asset_dimension: population
    description: Returnees to communities from internal and external displacement
      due to flood hazards
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_4
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
  url: https://dtm.iom.int/sites/g/files/tmzbdl1461/files/DTM%20Methodological%20Framework%20-%202nd%20Edition%202022_0.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM conducted the ACVA Round 2 in March and early April 2025 to capture
    climate and disaster data during the first quarter of 2025. The ACVA Round 2 estimated
    3,109,221 IDP individuals and 5,876,345 returnees from 2021 to the first quarter
    of 2025.
  download_url: https://data.humdata.org/dataset/1e6fc369-d98f-4689-be04-fbf23739979a/resource/05fb65fb-e677-4fbc-9efa-b7b586afa654/download/round_02_climate_vulnerability_assessment_data_may_2025_hdx.xlsx
  format: null
  id: resource_05fb65fb
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Round 02 Climate_Vulnerability_Assessment_Data May_2025_hdx.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: DTM conducted the ACVA Round 1 from November to January 2025 to capture
    climate and disaster data. The ACVA Round 1 estimated 2,971,985 IDP individuals
    and 5,314,754 returnees from 2021 to January 2025.
  download_url: https://data.humdata.org/dataset/1e6fc369-d98f-4689-be04-fbf23739979a/resource/6583c13e-5020-4950-8a06-f672880cf605/download/round_01_climate_vulnerability_assessment_data_jan_2025_hdx.xlsx
  format: null
  id: resource_6583c13e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Round 01 Climate_Vulnerability_Assessment_Data Jan_2025.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-afg_iom_displacementdataclimatevu_2024
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-05-31'
  start: '2024-11-03'
temporal_resolution: null
title: Afghanistan Displacement Data - Climate Vulnerability Assessment [IOM DTM]
version: null
vulnerability: null
---
