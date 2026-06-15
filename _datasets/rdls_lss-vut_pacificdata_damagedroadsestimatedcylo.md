---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: geodatarequest
  url: https://geonode.pacificdata.org/api/v2/users/1245
creator:
  affiliation: null
  email: null
  name: Pacific Community - SPC
  url: https://geonode.pacificdata.org/api/v2/users/1000
dataset_id: rdls_lss-vut_pacificdata_damagedroadsestimatedcylo
description: 'Output of RiskScape Cyclone-PDNA model which uses the SPC-generated
  hazard data to estimate cyclone losses/exposure for Vanuatu. [Source: This metadata
  record was automatically extracted from GeoNode portal pacificdata]'
details: null
exposure: []
hazard: null
license: CC-BY-NC-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geonode.pacificdata.org/catalogue/#/dataset/823
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: null
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: PGWS:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: loss_strong_wind
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: currency
          unit: null
        metric: loss
        modelling: inferred
        type: direct
      loss_approach: empirical
      loss_frequency_type: probabilistic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Earth and Oceans Observations Team Pacific Community
  url: https://geonode.pacificdata.org/catalogue/#/dataset/823
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (JSON)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_0
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://geonode.pacificdata.org/datasets/geonode:vu_cyclone_pdna_damaged_roads
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (OGC WMS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:vu_cyclone_pdna_damaged_roads&format=image%2Fpng
  format: null
  id: resource_1
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.pacificdata.org/datasets/geonode:vu_cyclone_pdna_damaged_roads
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (OGC WFS: geonode Service)'
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:vu_cyclone_pdna_damaged_roads&outputFormat=application%2Fjson
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
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (Zipped Shapefile)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
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
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (GML 2.0)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_4
  media_type: application/gml+xml
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GML 2.0
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (GML 3.1.1)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_5
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
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (CSV)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_6
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
  description: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA
    model output_ Vanuatu (Excel)
  download_url: https://geonode.pacificdata.org/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3Avu_cyclone_pdna_damaged_roads&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Excel
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-vut_pacificdata_damagedroadsestimatedcylo
spatial:
  bbox:
  - 166.84271049
  - -20.24941323
  - 169.78935579
  - -13.90757189
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Damaged roads from estimated cylone exposure_ RiskScape Cyclone PDNA model
  output_ Vanuatu
version: null
vulnerability: null
---
