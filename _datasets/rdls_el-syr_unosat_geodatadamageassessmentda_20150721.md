---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015
dataset_id: rdls_el-syr_unosat_geodatadamageassessmentda_20150721
description: 'This map illustrates satellite-detected damage in the city of Daraa,
  Syrian Arab Republic. Using satellite imagery acquired 04 June 2015, 01 May 2014,
  07 September 2013, and 14 December 2010, UNITAR - UNOSAT identified a total of 936
  affected structures within the extent of this map. Approximately 122 of these were
  destroyed, 355 severely damaged, and 459 moderately damaged. The city-wide analysis
  of Daraa revealed a total of 966 affected structures, of which 133 were destroyed,
  365 severely damaged, and 468 moderately damaged. Trend analysis shows an important
  increase in the number of damaged structures since 01 May 2014 and more than 600
  structures are newly damaged. This analysis was done of the REACH initiative for
  the U.S. Office of Foreign Disaster Assistance. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR -
  UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015]'
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
    description: Building stock in Daraa city classified by damage severity from satellite
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
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 14 December
    2010, 07 September 2013, 01 May 2014, and 04 June 2015 to detect notable changes
    in building structures. Damage was classified into three categories (destroyed,
    severely damaged, moderately damaged) through visual interpretation of satellite
    imagery, producing a spatial inventory of 966 affected structures across Daraa
    city.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-daraa-daraa-governorate-syria-july-21-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Daraa
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
  description: Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
  format: null
  id: resource_56f670a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
  format: null
  id: resource_3c2033f8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmentda_20150721
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-07-21'
temporal_resolution: null
title: Geodata of Damage Assessment of Daraa, Daraa Governorate, Syria
version: null
vulnerability: null
---
