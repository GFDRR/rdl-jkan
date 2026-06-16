---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damagedtadmur-and-al-miriyah-homs-governo-april-20-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damagedtadmur-and-al-miriyah-homs-governo-april-20-2016
dataset_id: rdls_el-syr_unosat_geodatapercentagesbuildin_20160420
description: 'This map illustrates percentages of buildings damaged in the cities
  of Tadmur and Al-Amiriyah in the Syrian Arab Republic as determined by satellite
  imagery analysis. Using satellite imagery acquired 30 March 2016, 18 October 2015,
  27 August 2015, and 26 June 2015, UNITAR-UNOSAT identified a total of 611 damaged
  structures within the extent of this map. These damaged structures are compared
  with total numbers of buildings found in a pre-conflict satellite image collected
  in 2009 to determine the percentage of damaged buildings across the cityt. This
  is a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damagedtadmur-and-al-miriyah-homs-governo-april-20-2016]'
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
    description: Building stock inventory in Tadmur and Al-Miriyah cities derived
      from 2009 pre-conflict satellite imagery
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (26 June
    2015, 27 August 2015, 18 October 2015, and 30 March 2016) against a 2009 pre-conflict
    baseline to identify damaged structures. A total of 611 damaged buildings were
    identified and mapped as polygons with damage percentage attributes calculated
    relative to total building counts from the baseline inventory.
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
- href: https://data.humdata.org/dataset/geodata-of-percentages-of-buildings-damagedtadmur-and-al-miriyah-homs-governo-april-20-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed through satellite imagery comparison
      between 2009 baseline and 2015-2016 post-conflict periods
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
  description: Geodata of Percentages of Buildings Damaged,Tadmur and Al-Miriyah,
    Homs Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330_shp.zip
  format: null
  id: resource_d040808b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Percentages of Buildings Damaged,Tadmur and Al-Miriyah,
    Homs Governorate, Syria (Shapefile)
  download_url: https://cern.ch/unosat-maps/SY/CE20130604SYR/Palmyra_Tadmur_20160330.gdb.zip
  format: null
  id: resource_5827723b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Palmyra_Tadmur_20160330.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-syr_unosat_geodatapercentagesbuildin_20160420
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
  start: '2016-04-20'
temporal_resolution: null
title: Geodata of Percentages of Buildings Damaged,Tadmur and Al-Miriyah, Homs Governorate,
  Syria
version: null
vulnerability: null
---
