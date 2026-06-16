---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-cavaillon-commune-sud-department-haiti
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-cavaillon-commune-sud-department-haiti
dataset_id: rdls_hzd-hti_unosat_detectedwaterextentcavail_20170427
description: 'This map illustrates the satellite-detected water extent in Cavaillon
  commune in Sud Department (Haiti) located in the southwestern part of Haiti. The
  UNITAR-UNOSAT analysis used a Sentinel-1 satellite image acquired on the 26 April
  2017 and a Radarsat-2 image acquired on the 17 May 2016 and could observe areas
  with standing waters mainly affecting agricultural fields. The UNITAR-UNOSAT analysis
  identified 566 ha of flooded areas, which cover 7% of this map''s extent of ~8500
  ha of land. The increase of waters within the analyzed zone is about 550%. ~100
  ha of surface waters were observed the 17 May 2016 and reached ~666 ha the 26 April
  2017. About 6km of roads, mainly local roads are potentially affected. It is likely
  that flood waters have been systematically underestimated along highly vegetated
  areas along main river banks and within built-up urban areas because of the special
  characteristics of the satellite data used. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-cavaillon-commune-sud-department-haiti]'
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared Sentinel-1 SAR imagery from 26 April 2017
    with Radarsat-2 imagery from 17 May 2016 to detect changes in water extent across
    Cavaillon commune. Standing water areas were identified and mapped as vector polygons
    with area calculations, resulting in a 550% increase in surface water detection
    (from ~100 ha to 566 ha) primarily affecting agricultural fields.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-cavaillon-commune-sud-department-haiti
  rel: source
loss: null
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
  description: Haiti - Satellite Detected Water Extent in Cavaillon Commune, Sud Department
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_gdb.zip
  format: Geodatabase
  id: resource_5a9bd740
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Satellite Detected Water Extent in Cavaillon Commune, Sud Department
    (Zipped shapefile.)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/FL20170424HTI/FL20170424HTI_SHP.zip
  format: null
  id: resource_658e796a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170424HTI_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_unosat_detectedwaterextentcavail_20170427
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-27'
temporal_resolution: null
title: Haiti - Satellite Detected Water Extent in Cavaillon Commune, Sud Department
version: null
vulnerability: null
---
