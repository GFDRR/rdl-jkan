---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied
dataset_id: rdls_hel-pse_unosat_seasurgeriskfloodimpactas_20250910
description: 'UNOSAT code: FL20250828PSE This map illustrates the current shoreline
  and the highest observed watermark in the Southern Gaza Strip (Occupied Palestinian
  Territory), derived from Sentinel-2 and Pleiades imagery acquired on 28 July 2025
  and 29 August 2025, respectively. The analysis focuses on the area west of Al Rashid
  Road, where a very high density of tents has been observed within a small geographic
  area that is particularly prone to flooding in the event of high tides or storm
  surges. UNITAR-UNOSAT has identified 2,367 shelters/tents in high-risk areas (within
  20 meters of the highest observed watermark) and 3,631 shelters/tents in risk areas
  (within 50 meters of the highest observed watermark). This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied]'
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
    description: Shelters and tents identified in high-risk coastal flood zones within
      20 meters of observed watermark
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
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-2 (28 July 2025) and Pleiades (29 August 2025) satellite imagery
    were analyzed by UNOSAT to identify the current shoreline and highest observed
    watermark in Southern Gaza Strip. Shelters and tents within 20 meters of the watermark
    in high-density settlement areas were manually delineated and counted to assess
    exposure to coastal flooding and storm surge hazards.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-southern-gaza-strip-occupied
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of shelters/tents at risk from coastal flooding and storm surge
      in Southern Gaza Strip
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Sea Surge risk & flood impact assessment in the Coastal
    Area of Southern Gaza Strip (Occupied Palestinian Territory) as of 29 August 2025
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4200/FL20250828PSE_gdb.zip
  format: Geodatabase
  id: resource_db21c2bc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250828PSE_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Sea Surge risk & flood impact assessment in the Coastal
    Area of Southern Gaza Strip (Occupied Palestinian Territory) as of 29 August 2025
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4200/FL20250828PSE_SHP.zip
  format: null
  id: resource_ade56463
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250828PSE_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pse_unosat_seasurgeriskfloodimpactas_20250910
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-10'
temporal_resolution: null
title: Palestine - Sea Surge risk & flood impact assessment in the Coastal Area of
  Southern Gaza Strip (Occupied Palestinian Territory) as of 29 August 2025
version: null
vulnerability: null
---
