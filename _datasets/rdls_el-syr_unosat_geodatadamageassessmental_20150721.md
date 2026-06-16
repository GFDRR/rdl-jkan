---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015
dataset_id: rdls_el-syr_unosat_geodatadamageassessmental_20150721
description: 'This map illustrates satellite-detected damage in a portion of the city
  of Aleppo, Syrian Arab Republic. Using satellite imagery acquired 01 May 2015, 26
  April 2015, 23 May 2014, 23 September 2013, and 21 November 2010, UNITAR - UNOSAT
  identified a total of 5,170 affected structures within the extent of this map. Approximately
  904 of these were destroyed, 2,641 severely damaged, and 1,625 moderately damaged.
  The city-wide analysis of Aleppo revealed a total of 14,034 affected structures,
  of which 2,878 were destroyed, 6,879 severely damaged, and 4,277 moderately damaged.
  While much of the city was damaged by 23 May 2014, 5,567 structures were newly damaged
  and 90 structures experienced an increase in damage between that date and 01 May
  2015. This analysis was done of the REACH initiative for the U.S. Office of Foreign
  Disaster Assistance. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015]'
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
    description: Building stock classified by damage severity (destroyed, severely
      damaged, moderately damaged)
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
  description: UNOSAT analysts compared satellite imagery acquired on multiple dates
    (21 November 2010, 23 September 2013, 23 May 2014, 26 April 2015, 01 May 2015)
    to identify notable structural changes and classify affected buildings in Aleppo
    by damage severity (destroyed, severely damaged, moderately damaged). Building
    footprints and damage classifications were vectorized into shapefiles with damage
    category attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-july-21-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Aleppo
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
  description: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130404SYR_DamageAssessment_OFDA_REACH_UPDATE3_shp.zip
  format: null
  id: resource_90244bcd
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
  description: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_CE20130604SYR_OFDA_REACH_DA_UPDATE3.gdb.zip
  format: null
  id: resource_2d3b3491
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
slug: rdls_el-syr_unosat_geodatadamageassessmental_20150721
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
title: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria
version: null
vulnerability: null
---
