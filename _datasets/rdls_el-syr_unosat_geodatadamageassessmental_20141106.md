---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-november-06-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-november-06-2014
dataset_id: rdls_el-syr_unosat_geodatadamageassessmental_20141106
description: 'This map illustrates satellite-detected damage and destruction in a
  portion of the city of Aleppo, Aleppo Governorate, Syria. Using satellite imagery
  acquired 23 May 2014, 23 September 2013, and 21 November 2010, UNITAR / UNOSAT identified
  a total of 3,875 affected structures within the area of this map. Approximately
  630 of these were destroyed, 2,127 severely damaged, and 1,118 moderately damaged.
  The city-wide analysis of Aleppo revealed a total of 8,510 affected structures,
  of which 1,543 were destroyed, 4,847 severely damaged, and 2,120 moderately damaged.
  While much of the city was damaged by 23 Sepetember 2013, 7,937 structures were
  newly damaged and 17 structures experienced an increase in damage between that date
  and 23 May 2014. This analysis was done of the REACH initiative for the U.S. Office
  of Foreign Disaster Assistance. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-november-06-2014]'
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
    description: Building stock in Aleppo city classified by damage severity from
      satellite imagery
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
  description: UNOSAT analysts compared multi-temporal satellite imagery acquired
    on 21 November 2010, 23 September 2013, and 23 May 2014 to identify notable changes
    in building structures. Damage was classified into three categories (destroyed,
    severely damaged, moderately damaged) through visual interpretation, resulting
    in a spatial inventory of 8,510 affected structures across Aleppo city.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-aleppo-aleppo-governorate-syria-november-06-2014
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
  description: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR_shp.zip
  format: null
  id: resource_8a0f97f5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR.gdb.zip
  format: null
  id: resource_5927f529
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_DamageAssessment_OFDA-REACH_CE20130604SYR.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatadamageassessmental_20141106
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
  start: '2014-11-06'
temporal_resolution: null
title: Geodata of Damage Assessment of Aleppo, Aleppo Governorate, Syria
version: null
vulnerability: null
---
