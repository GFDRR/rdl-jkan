---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Food and Agriculture Organization (FAO)
    url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024
dataset_id: rdls_el-pse_unosat_faostripcroplanddamageass_20240830
description: 'UNOSAT code: CE20231007PSE This map illustrates satellite-detected changes
  in cropland areas of the Gaza Strip resulting from the decline in the health and
  density of crops due to the ongoing conflict. UNOSAT conducted an analysis utilising
  satellite imagery collected by the Sentinel-2 satellite between August 2017 and
  2024, performing a Normalized Difference Vegetation Index (NDVI) analysis as well
  as a multitemporal classification to identify notable changes taking place in agricultural
  areas during that timeframe. The methodology evaluated the damage as a decline in
  the health and density of crops in August 2024, in comparison to the preceding seven
  seasons spanning from 2017 to 2024. The decline in the health and density of the
  crops can be observed due to the impact of activities such as razing, heavy vehicle
  activity, bombing, shelling, and other conflict-related dynamics. The analysis includes
  damage assessment for orchards and other trees, field crops and vegetables. UNOSAT
  analysis shows that the agricultural extent in the Gaza Strip is estimated to be
  150 sq. km, accounting for approximately 41% of the total area of the Gaza Strip,
  following an extensive land-cover analysis. Compared to the average of the previous
  seven years, approximately 68% of the permanent crop fields in the Gaza Strip exhibited
  a significant decline in health and density in August 2024. In a comprehensive evaluation,
  it was found that there has been a 4% increase in the proportion of cropland that
  has been damaged since the previous analysis conducted in July 2024. Additionally,
  the analysis indicates a notable rise in the destruction of the orchards and other
  trees, field crops and vegetables in the Deir al-Balah Governorate, with a 5-percentage
  point increase compared to the previous July 2024 analysis. Moreover, there has
  been a notable escalation in the destruction of cropland within the Gaza Governorate,
  with the percentage rising from 73% in July 2024 to 75% in August 2024. This is
  a preliminary analysis and has not yet been validated in the field.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024]'
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
    description: Cropland areas in Gaza Strip classified by vegetation health and
      density status
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Sentinel-2 satellite imagery spanning August 2017 to August 2024 was
    processed using Normalized Difference Vegetation Index (NDVI) analysis and multitemporal
    classification to detect changes in cropland health and density. Satellite-detected
    vegetation decline in agricultural areas was mapped as direct crop damage resulting
    from the ongoing conflict, with results delivered as a geodatabase containing
    classified agricultural damage zones.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Food and Agriculture Organization (FAO)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-fao-gaza-strip-cropland-damage-assessment-august-2024
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural damage from crop decline detected via satellite
      vegetation index analysis
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
          quantity_kind: area
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
  description: Palestine - UNOSAT - FAO Gaza Strip Cropland Damage Assessment - August
    2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3939/FAO-PAL-010_UNOSAT_Agriculture_DA_GDB_Aug2024_v2.zip
  format: Geodatabase
  id: resource_033a18fb
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FAO-PAL-010_UNOSAT_Agriculture_DA_GDB_Aug2024_v2.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_faostripcroplanddamageass_20240830
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
  start: '2024-08-30'
temporal_resolution: null
title: Palestine - UNOSAT - FAO Gaza Strip Cropland Damage Assessment - August 2024
version: null
vulnerability: null
---
