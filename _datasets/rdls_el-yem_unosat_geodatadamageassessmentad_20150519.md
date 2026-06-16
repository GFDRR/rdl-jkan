---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aden-aden-governorate-yemen-may-19-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aden-aden-governorate-yemen-may-19-2015
dataset_id: rdls_el-yem_unosat_geodatadamageassessmentad_20150519
description: 'This map illustrates satellite-detected damage and destruction in the
  city of Aden, Aden Governorate, Yemen. Using satellite imagery acquired 10 May 2015,
  15 April 2015, and 31 December 2014, UNITAR-UNOSAT identified a total of 642 affected
  structures, 258 of which were temporarily assembled for a probable open street market.
  Approximately 327 structures were destroyed, 153 severely damaged, and 162 moderately
  damaged. Additionally, 38 impact craters were found within the city, the majority
  of which were located in the vicinity of Aden International Airport. A total of
  13 medical facilities were identified within 100 meters of damaged and destroyed
  buildings, and it is possible that these facilities also sustained some damage.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aden-aden-governorate-yemen-may-19-2015]'
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
    description: Building stock in Aden city classified by damage state from satellite
      imagery
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
    description: Medical facilities and airport infrastructure affected by conflict-related
      damage
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    on 31 December 2014, 15 April 2015, and 10 May 2015 to identify and classify damage
    to buildings and infrastructure in Aden city. Damage was categorized into destruction,
    severe damage, and moderate damage states through visual interpretation of satellite-detected
    changes. The resulting geodataset contains 642 affected structures with confidence
    levels and validation flags.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aden-aden-governorate-yemen-may-19-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from conflict-related impacts (642 affected
      structures: 327 destroyed, 153 severely damaged, 162 moderately damaged)'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage including 13 medical facilities and
      38 impact craters near Aden International Airport
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: Geodata of Damage Assessment of Aden, Aden Governorate, Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_shp.zip
  format: null
  id: resource_dfcd6b6b
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
  description: Geodata of Damage Assessment of Aden, Aden Governorate, Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_gdb.zip
  format: null
  id: resource_6dff391d
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
slug: rdls_el-yem_unosat_geodatadamageassessmentad_20150519
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
  start: '2015-05-19'
temporal_resolution: null
title: Geodata of Damage Assessment of Aden, Aden Governorate, Yemen
version: null
vulnerability: null
---
