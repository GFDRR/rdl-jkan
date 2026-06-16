---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-international-airport-sanaa-governorate-june-03-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-international-airport-sanaa-governorate-june-03-2015
dataset_id: rdls_el-yem_unosat_geodatadamageassessmentsa_20150603
description: 'This map illustrates satellite-detected damage and destruction at Sana''a
  International Airport, Sana''a Governorate, Yemen. Using satellite imagery acquired
  15 May 2015 and 12 December 2014, UNITAR-UNOSAT identified a total of 70 affected
  structures and transportation vehicles. Approximately 18 of these were destroyed,
  32 severely damaged, and 20 moderately damaged. Additionally, 32 impact craters
  were found. One medical facility was identified within 500 meters of impact craters.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-international-airport-sanaa-governorate-june-03-2015]'
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
    description: Airport infrastructure including runway, taxiways, and terminal facilities
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Structures at Sana'a International Airport including hangars and
      support buildings
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
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
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    (12 December 2014 and 15 May 2015) of Sana'a International Airport to identify
    and classify damage to structures and infrastructure. Damage was categorized into
    destruction, severe damage, and moderate damage classes, with impact craters and
    nearby medical facilities also mapped. This preliminary analysis was based on
    satellite-detected changes without field validation.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-sanaa-international-airport-sanaa-governorate-june-03-2015
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to airport infrastructure from conflict-related impacts
      detected via satellite imagery
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct damage to structures at airport (18 destroyed, 32 severely
      damaged, 20 moderately damaged)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Geodata of Damage Assessment of Sana'a International Airport, Sana'a
    Governorate, Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_shp.zip
  format: null
  id: resource_c16a5642
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
  description: Geodata of Damage Assessment of Sana'a International Airport, Sana'a
    Governorate, Yemen (Shapefile)
  download_url: https://cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_gdb.zip
  format: null
  id: resource_4d744a23
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
slug: rdls_el-yem_unosat_geodatadamageassessmentsa_20150603
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
  start: '2015-06-03'
temporal_resolution: null
title: Geodata of Damage Assessment of Sana'a International Airport, Sana'a Governorate,
  Yemen
version: null
vulnerability: null
---
