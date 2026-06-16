---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-neighborhoods-in-western-benghazi-city-libya-august-12-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-neighborhoods-in-western-benghazi-city-libya-august-12-2016
dataset_id: rdls_lss-lby_unosat_geodatadamageassessmentne_20160812
description: 'This map illustrates satellite-detected areas of damage in the Al Thama,
  Al Sabri, Old Benghazi, Al Salmane Al Sharge, and Al Salmane Al Garbe neighborhoods
  of Benghazi City, Libya. Using satellite imagery acquired 04 and 19 April 2016 as
  well as 01 August 2015, UNITAR-UNOSAT identified a total of 1,184 potentially damaged
  structures in these neighborhoods. Approximately 75 of these were destroyed, 198
  severely damaged, 426 moderately damaged, and 485 possibly damaged. A slightly higher
  margin of error is possible in this analysis due to utilization of multiple images
  and the uncontrolled nature of construction in Benghazi during the analysis timeframe.
  This is a preliminary analysis & has not yet been validated in the field. Please
  send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-neighborhoods-in-western-benghazi-city-libya-august-12-2016]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 01 August 2015,
    04 April 2016, and 19 April 2016 to detect changes in building conditions across
    five Benghazi neighborhoods. Damaged structures were classified into four severity
    categories (destroyed, severely damaged, moderately damaged, possibly damaged)
    based on visual interpretation of satellite-detected changes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-neighborhoods-in-western-benghazi-city-libya-august-12-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from satellite imagery comparison
      in Benghazi neighborhoods
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: 'Geodata of Damage Assessment: Neighborhoods in Western Benghazi City,
    Libya (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LY/CE20150814LBY/Benghazi_20160419_Update_shp.zip
  format: null
  id: resource_922290b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Benghazi_20160419_Update_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Geodata of Damage Assessment: Neighborhoods in Western Benghazi City,
    Libya (Shapefile)'
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LY/CE20150814LBY/Benghazi_20160419_Update.gdb.zip
  format: null
  id: resource_c4bf2ad6
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Benghazi_20160419_Update.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_unosat_geodatadamageassessmentne_20160812
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-12'
temporal_resolution: null
title: 'Geodata of Damage Assessment: Neighborhoods in Western Benghazi City, Libya'
version: null
vulnerability: null
---
