---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri
dataset_id: rdls_lss-mmr_unosat_damageassessmentmahaaungm_20250402
description: 'UNOSAT code: EQ20250328MMR, GDACS ID: 1474477 This map illustrates the
  density of damaged buildings affected by the March 28, 2025, earthquake in Mandalay.
  The analysis focuses on Mahaaungmyay, Chanmyathazi, and Chanayethazan Townships
  in Mandalay District, Mandalay Region, where damage was detected using a Pleiades
  very high-resolution satellite image acquired on March 30, 2025, at 11:01 local
  time. UNOSAT identified 509 damaged structures and 284 potentially damaged. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri]'
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
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    (acquired March 30, 2025) to detect structural damage from the March 28, 2025
    earthquake. Damaged buildings were identified through visual interpretation of
    satellite imagery and classified by confidence level and damage severity in three
    townships of Mandalay District, Myanmar.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-mahaaungmyay-chanmyathazi-and-chanayethazan-townships-mandalay-distri
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the March 28, 2025 earthquake in Mandalay,
      detected via satellite imagery
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
  description: Damage Assessment in Mahaaungmyay, Chanmyathazi and Chanayethazan Townships,
    Mandalay District, Mandalay Region, Myanmar as of 30 March 2025 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4094/EQ20250328MMR_gdb.zip
  format: Geodatabase
  id: resource_5da16a40
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Mahaaungmyay, Chanmyathazi and Chanayethazan Townships,
    Mandalay District, Mandalay Region, Myanmar as of 30 March 2025 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4094/EQ20250328MMR_SHP.zip
  format: null
  id: resource_26efafd9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20250328MMR_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mmr_unosat_damageassessmentmahaaungm_20250402
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-02'
temporal_resolution: null
title: Damage Assessment in Mahaaungmyay, Chanmyathazi and Chanayethazan Townships,
  Mandalay District, Mandalay Region, Myanmar as of 30 March 2025
version: null
vulnerability: null
---
