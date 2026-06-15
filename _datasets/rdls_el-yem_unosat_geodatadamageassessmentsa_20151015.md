---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-city-sanaa-governorate-yemen-october-15-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-city-sanaa-governorate-yemen-october-15-2015
dataset_id: rdls_el-yem_unosat_geodatadamageassessmentsa_20151015
description: 'This map illustrates satellite-detected damage and destruction in the
  city of Sana''a, Sana''a Governorate, Yemen. Using satellite imagery acquired 10
  and 23 September 2015, as well as 15 May 2015, UNITAR-UNOSAT identified a total
  of 652 affected structures. Approximately 283 of these were impacted as of 10 and
  23 September 2015, with 54 destroyed, 94 severely damaged, and 135 moderately damaged.
  Previously, using the 15 May 2015 satellite image, UNITAR-UNOSAT had located 369
  affected structures, of which 60 were destroyed, 72 severely damaged, and 237 moderately
  damaged. Additionally, 8 impact craters and 16 areas with significant amounts of
  debris were observed in September 2015. A total of 7 medical facilities were identified
  within 100 meters of damaged and destroyed buildings, and it is possible that these
  facilities also sustained some damage. Notably, as of 10 and 23 September 2015,
  significant reconstruction of structures damaged as of 15 May 2015 was visible across
  the examined area. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-city-sanaa-governorate-yemen-october-15-2015]'
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
    description: Building stock in Sana'a city classified by damage severity from
      satellite-detected assessment
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 15 May 2015,
    10 September 2015, and 23 September 2015 to detect notable changes in building
    structures. Damage was classified into destroyed, severely damaged, and moderately
    damaged categories through visual interpretation of satellite imagery. The resulting
    geodataset contains 652 affected structures with spatial geometry and damage classification
    attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-city-sanaa-governorate-yemen-october-15-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction detected
      via satellite imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Geodata of Damage Assessment of Sana'a City, Sana'a Governorate, Yemen
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_shp.zip
  format: null
  id: resource_afb0211a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20150402YEM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Sana'a City, Sana'a Governorate, Yemen
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_gdb.zip
  format: null
  id: resource_59bf9613
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20150402YEM_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_unosat_geodatadamageassessmentsa_20151015
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-15'
temporal_resolution: null
title: Geodata of Damage Assessment of Sana'a City, Sana'a Governorate, Yemen
version: null
vulnerability: null
---
