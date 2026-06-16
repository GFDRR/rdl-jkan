---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-ramadi-al-anbar-province-iraq-january-15-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-ramadi-al-anbar-province-iraq-january-15-2016
dataset_id: rdls_el-irq_unosat_geodatadamageassessmentce_20160115
description: 'This map illustrates satellite-detected damage and destruction in Ramadi
  City, Iraq. Using satellite imagery collected 29 January 2016 collected by the GeoEye-1
  satellite, and compared with a pre-crisis Pleiades image collected 06 July 2014,
  UNOSAT analysis has identified 1,165 destroyed structures, 818 severely damaged
  structures, and 1,222 moderately damaged structures within the downtown area of
  Ramadi. Considerably more damage is found in surrounding areas of the city (not
  shown on map). Note that this analysis documents destruction occurring between 6
  July 2014 and 29 January 2016, certain areas of Ramadi show destruction occurring
  prior to 6 July 2014. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-ramadi-al-anbar-province-iraq-january-15-2016]'
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
    description: Building stock in central Ramadi classified by damage severity (destroyed,
      severely damaged, moderately damaged)
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
  description: UNOSAT analysts compared multi-temporal satellite imagery (Pleiades
    pre-crisis baseline from July 2014 and GeoEye-1 post-event from January 2016)
    to identify structural changes and classify buildings into three damage categories
    (destroyed, severely damaged, moderately damaged) through visual interpretation.
    The resulting geodataset contains 3,205 classified building damage records with
    spatial geometry and confidence assessments for downtown Ramadi.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-central-ramadi-al-anbar-province-iraq-january-15-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related destruction
      in Ramadi
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
  description: Geodata of Damage Assessment in Central Ramadi, Al Anbar Province,
    Iraq (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Ramadi_20160129_shp.zip
  format: null
  id: resource_d802fd61
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Ramadi_20160129_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment in Central Ramadi, Al Anbar Province,
    Iraq (Shapefile)
  download_url: https://cern.ch/unosat-maps/IQ/CE20140613IRQ/CE20140613IRQ_Ramadi_20160129_gdb.zip
  format: null
  id: resource_1397754e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140613IRQ_Ramadi_20160129_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-irq_unosat_geodatadamageassessmentce_20160115
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-01-15'
temporal_resolution: null
title: Geodata of Damage Assessment in Central Ramadi, Al Anbar Province, Iraq
version: null
vulnerability: null
---
