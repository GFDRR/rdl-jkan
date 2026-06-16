---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Space Agency Sentinel-1
    url: https://data.humdata.org/dataset/cloud-to-street-rohingya-refugees-flood-maps-2018-06-13-based-on-sentinel-1-imagery
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Cloud to Street (inactive)
  url: https://data.humdata.org/dataset/cloud-to-street-rohingya-refugees-flood-maps-2018-06-13-based-on-sentinel-1-imagery
creator:
  affiliation: null
  email: null
  name: Cloud to Street (inactive)
  url: https://data.humdata.org/dataset/cloud-to-street-rohingya-refugees-flood-maps-2018-06-13-based-on-sentinel-1-imagery
dataset_id: rdls_hzd-bgd_cloud_to_street_rohingyarefugeesfloodmaps_20180613
description: 'Includes a binary GeoTIFF where 0 values are non-flooded and 1 values
  are flooded. Included a metadata file that describes a summary and methods for the
  data.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cloud-to-street-rohingya-refugees-flood-maps-2018-06-13-based-on-sentinel-1-imagery]'
details: null
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
      process: pluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Sentinel-1 SAR satellite imagery from 13 June 2018 was processed to
    classify pixels as flooded (1) or non-flooded (0) using radar backscatter analysis,
    producing a binary flood extent map for the Rohingya megacamp in Cox's Bazar,
    Bangladesh.
  sources:
  - id: source_1
    license: null
    name: European Space Agency Sentinel-1
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cloud-to-street-rohingya-refugees-flood-maps-2018-06-13-based-on-sentinel-1-imagery
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
  description: Bangladesh - Cloud to Street Rohingya Refugees Flood Maps based on
    Sentinel-1 Imagery (Flood map GeoTIFF)
  download_url: https://data.humdata.org/dataset/4df67e9c-04a1-4d35-91ac-553c524b3ad3/resource/b7287bb7-c8d8-430b-9a05-422fbd499ebb/download/rohingya_megacamp_flood_sentinel1_20180613_cloudtostreet.tif
  format: null
  id: resource_b7287bb7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rohingya_Megacamp_Flood_Sentinel1_20180613_CloudToStreet.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Cloud to Street Rohingya Refugees Flood Maps based on
    Sentinel-1 Imagery (Flood map metadata)
  download_url: https://data.humdata.org/dataset/4df67e9c-04a1-4d35-91ac-553c524b3ad3/resource/0fda4539-4368-4b46-8e9a-5e3923c000cb/download/rohingya_megacamp_flood_sentinel1_20180613_metadata_cloudtostreet.pdf
  format: null
  id: resource_0fda4539
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rohingya_Megacamp_Flood_Sentinel1_20180613_Metadata_CloudToStreet.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Cloud to Street Rohingya Refugees Flood Maps based on
    Sentinel-1 Imagery (Flood map shapefiles)
  download_url: https://data.humdata.org/dataset/4df67e9c-04a1-4d35-91ac-553c524b3ad3/resource/1ff0ba59-7c71-4f2f-a1d2-c24628c41260/download/rohingya_megacamp_flood_sentinel1_20180613_cloudtostreet.zip
  format: null
  id: resource_1ff0ba59
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Rohingya_Megacamp_Flood_Sentinel1_20180613_CloudtoStreet.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_cloud_to_street_rohingyarefugeesfloodmaps_20180613
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-06-13'
temporal_resolution: null
title: Bangladesh - Cloud to Street Rohingya Refugees Flood Maps based on Sentinel-1
  Imagery
version: null
vulnerability: null
---
