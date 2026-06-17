---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-11-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-11-2014
dataset_id: rdls_hzd-zwe_unosat_geodatafloodwaterovertokw_20140211
description: 'This map illustrates satellite-detected water bodies at the Tokwe Mukorsi
  Dam, Masvingo Province, Zimbabwe, as detected by TerraSAR-X on 11 February 2014.
  The flooded area above the dam has greatly increased due to recent heavy rains and
  currently encompasses about 2,300 ha. It is likely that flood waters have been systematically
  underestimated along highly vegetated areas along main river banks because of the
  special characteristics of the satellite data used. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR /UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-11-2014]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts processed TerraSAR-X satellite imagery acquired on
    11 February 2014 over Tokwe Mukorsi Dam, comparing imagery to detect water body
    changes and delineate flooded areas. The resulting flood extent polygons were
    digitized and attributed with area measurements in hectares and square meters.
    Vegetation masking limitations are noted as a source of potential underestimation
    in densely vegetated riparian zones.
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
- href: https://data.humdata.org/dataset/geodata-of-flood-water-over-tokwe-mukorsi-dam-masvingo-province-zimbabwe-february-11-2014
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
- access_url: https://unosatgis.cern.ch/arcgis/rest/services/FL/FP01_FL_20140207_ZWE_Flood_20140211_TerraSARX/MapServer/kml/mapImage.kmz
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Water over Tokwe Mukorsi Dam, Masvingo Province, Zimbabwe
    (KMZ)
  download_url: null
  format: null
  id: resource_c516a148
  media_type: application/vnd.google-earth.kmz
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mapImage.kmz
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Water over Tokwe Mukorsi Dam, Masvingo Province, Zimbabwe
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/FL20140207ZWE_shp.zip
  format: null
  id: resource_a0835a5e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140207ZWE_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Water over Tokwe Mukorsi Dam, Masvingo Province, Zimbabwe
    (KML)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZW/FL20140207ZWE/FL20140207ZWE.gdb.zip
  format: null
  id: resource_ce580203
  media_type: application/vnd.google-earth.kml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20140207ZWE.gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-zwe_unosat_geodatafloodwaterovertokw_20140211
spatial:
  bbox: null
  centroid: null
  countries:
  - ZWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-02-11'
temporal_resolution: null
title: Geodata of Flood Water over Tokwe Mukorsi Dam, Masvingo Province, Zimbabwe
version: null
vulnerability: null
---
