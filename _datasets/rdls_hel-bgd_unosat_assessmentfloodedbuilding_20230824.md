---
attributions:
- entity:
    affiliation: null
    email: null
    name: Microsoft building footprint dataset
    url: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data (2020)
    url: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Satellite imagery
    url: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
dataset_id: rdls_hel-bgd_unosat_assessmentfloodedbuilding_20230824
description: 'UNOSAT code FL20230807BGD This map illustrate the number of affected
  buildings within specific district boundaries of interest in Bandarban, Cox''s Bazar,
  Chattogram, and Rangamati Districts, located in Chattogram Division, Bangladesh
  as of 12 to August 2023. And using an automated analysis with Artificial Intelligence
  based methods. Within the analyzed area of about 17,000 km2 and, about 350km2 of
  lands appear to be flooded. Based on Worldpop population data from 2020, the flood
  water extent and Microsoft building footprint , ~415,000 people are potentially
  exposed or living close to flooded areas and about 932 building potentially affected
  by floods. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Building footprints from Microsoft dataset within the flood-affected
      districts
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Residential population from WorldPop 2020 data potentially exposed
      to flood waters
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed multi-temporal satellite imagery using artificial\
    \ intelligence-based automated analysis methods to delineate flood extent (~350\
    \ km\xC2\xB2) across four districts in Chattogram Division. Building footprints\
    \ from Microsoft and population data from WorldPop 2020 were spatially intersected\
    \ with the mapped flood extent to quantify affected buildings and exposed population\
    \ during the August 2023 flooding event."
  sources:
  - id: source_1
    license: null
    name: Microsoft building footprint dataset
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WorldPop population data (2020)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_3
    license: null
    name: Satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/assessment-of-flooded-buildings-in-bandarban-cox-s-bazaar-chattogram-and-rangamati-distric
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Number of affected buildings identified through satellite imagery
      analysis in flooded areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to flooding based on flood extent
      and population distribution
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Assessment of Flooded Buildings in Bandarban, Cox's Bazaar, Chattogram,
    and Rangamati Districts, Chattogram Division, Bangladesh as of 12 to 22 August
    2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3660/UNOSAT_FloodAssessment_FL20230807BGD_24Aug2023.xlsx
  format: null
  id: resource_c865350c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FloodAssessment_FL20230807BGD_24Aug2023.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_assessmentfloodedbuilding_20230824
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-08-24'
temporal_resolution: null
title: Assessment of Flooded Buildings in Bandarban, Cox's Bazaar, Chattogram, and
  Rangamati Districts, Chattogram Division, Bangladesh as of 12 to 22 August 2023
version: null
vulnerability: null
---
