---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/820
creator:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/820
dataset_id: rdls_hzd-vut_pacificdata_cyclonetrackriskscapecycl
description: 'Output of RiskScape Cyclone-PDNA model which uses the SPC-generated
  hazard data to estimate cyclone losses/exposure for Vanuatu. [Source: This metadata
  record was automatically extracted from the GeoNode portal pacificdata]'
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: Earth and Oceans Observations Team Pacific Community
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/820
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org
purpose: The RiskScape model that generated this dataset was developed as part of
  the PARTneR 2 project, funded by the New Zealand Ministry of Foreign Affairs and
  Trade (MFAT) and was jointly delivered by the Pacific Community (SPC) and NIWA,
  in collaboration with the partner countries. The project aims to help countries
  in the Pacific become more resilient to the impacts of climate-related hazards,
  while building on the pilot PARTneR project, which ran from 2016-2019. The project
  activities included co-developing national risk models and assessment tools.
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (GML 2.0)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_0
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: https://geonode.pacificdata.org/datasets/geonode:vu_cyclone_pdna_cyclone_track
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (OGC WMS:
    geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:vu_cyclone_pdna_cyclone_track&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:vu_cyclone_pdna_cyclone_track
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (OGC WFS:
    geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:vu_cyclone_pdna_cyclone_track&outputFormat=application%2Fjson
  format: null
  id: resource_2
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (Zipped
    Shapefile)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
  format: null
  id: resource_3
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (GML 3.1.1)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 3.1.1
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (CSV)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_5
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CSV
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (Excel)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_6
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu (JSON)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_cyclone_track&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_7
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vut_pacificdata_cyclonetrackriskscapecycl
spatial:
  bbox:
  - 165.91459
  - -18.65625
  - 169.4
  - -12.7
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2024
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Cyclone track, RiskScape Cyclone PDNA model output, Vanuatu
version: null
vulnerability: null
---
