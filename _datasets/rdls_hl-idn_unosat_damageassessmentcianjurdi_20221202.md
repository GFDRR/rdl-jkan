---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-cianjur-district-jawa-barat-province-indonesia-as-of-29-november-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-cianjur-district-jawa-barat-province-indonesia-as-of-29-november-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-cianjur-district-jawa-barat-province-indonesia-as-of-29-november-2022
dataset_id: rdls_hl-idn_unosat_damageassessmentcianjurdi_20221202
description: "UNOSAT code EQ20221121IDN, GDACS Id: 1347183 This map illustrates potentially\
  \ damaged structures and damaged structures in Cianjur district, Jawa Barat Province,\
  \ Indonesia as detected by a Pl\xE9iades image acquired on 29 November 2022 at 11:05\
  \ local time. Within the analyzed area, UNOSAT has identified 406 potentially damaged\
  \ structures, 35 damaged structures. This is a preliminary analysis and has not\
  \ yet been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-cianjur-district-jawa-barat-province-indonesia-as-of-29-november-2022]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: earthquake
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Pl\xE9iades satellite imagery acquired on\
    \ 29 November 2022 and compared it with reference imagery to identify structural\
    \ damage in Cianjur district following the 21 November 2022 earthquake. Damage\
    \ was classified into two categories: potentially damaged structures (406) and\
    \ confirmed damaged structures (35). This is a preliminary remote-sensing-based\
    \ assessment not yet validated through field surveys."
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-cianjur-district-jawa-barat-province-indonesia-as-of-29-november-2022
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from earthquake: 406 potentially damaged
      structures and 35 confirmed damaged structures'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Damage Assessment in Cianjur district, Jawa Barat Province, Indonesia
    as of 29 November 2022 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3458/EQ20221121IDN_gdb.zip
  format: Geodatabase
  id: resource_d0db6f89
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20221121IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Cianjur district, Jawa Barat Province, Indonesia
    as of 29 November 2022 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3458/EQ20221121IDN_SHP.zip
  format: null
  id: resource_5cda5327
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20221121IDN_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_unosat_damageassessmentcianjurdi_20221202
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-12-02'
temporal_resolution: null
title: Damage Assessment in Cianjur district, Jawa Barat Province, Indonesia as of
  29 November 2022
version: null
vulnerability: null
---
