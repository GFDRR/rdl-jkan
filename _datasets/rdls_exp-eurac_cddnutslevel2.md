---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: andrea.vianello@eurac.edu
  name: Andrea Vianello
  url: https://maps.eurac.edu/api/v2/users/1000
creator:
  affiliation: null
  email: andrea.vianello@eurac.edu
  name: Andrea Vianello
  url: https://maps.eurac.edu/api/v2/users/1000
dataset_id: rdls_exp-eurac_cddnutslevel2
description: 'Cooling Degree Day (CDD) index is a weather-based technical index designed
  to describe the need for the heating energy requirements of buildings. HDD is derived
  from meteorological observations of air temperature, interpolated to regular grids
  at 25 km resolution for Europe. Calculated gridded HDD is aggregated and subsequently
  presented on NUTS-2 level. [Source: This metadata record was automatically extracted
  from the GeoNode portal eurac]'
details: null
exposure:
- asset_type: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Dataset available on Eurostat portal https://ec.europa.eu/eurostat/cache/metadata/en/nrg_chdd_esms.htm
    The table is merged with the NUTS2 layer.
  sources:
  - id: source_1
    license: null
    name: Andrea Vianello
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/60
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Andrea Vianello
  url: https://maps.eurac.edu
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: CDD - NUTS level 2 (GML 2.0)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=gml2&srs=EPSG%3A4326
  format: null
  id: resource_0
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
  description: CDD - NUTS level 2 (GML 3.1.1)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A4326
  format: null
  id: resource_1
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
  description: CDD - NUTS level 2 (CSV)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=csv&srs=EPSG%3A4326
  format: null
  id: resource_2
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
  description: CDD - NUTS level 2 (Zipped Shapefile)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=SHAPE-ZIP&srs=EPSG%3A4326&format_options=charset%3AUTF-8
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
  description: CDD - NUTS level 2 (Excel)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=excel&srs=EPSG%3A4326
  format: null
  id: resource_4
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
  description: CDD - NUTS level 2 (JSON)
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3ACDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=json&srs=EPSG%3A4326&srsName=EPSG%3A4326
  format: null
  id: resource_5
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:CDD_Nuts_RG_01M_2021_4326_level_2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'CDD - NUTS level 2 (OGC WMS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:CDD_Nuts_RG_01M_2021_4326_level_2&format=image%2Fpng
  format: null
  id: resource_6
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://maps.eurac.edu/datasets/geonode:geonode:CDD_Nuts_RG_01M_2021_4326_level_2
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:4326
  description: 'CDD - NUTS level 2 (OGC WFS: geonode Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:geonode:CDD_Nuts_RG_01M_2021_4326_level_2&outputFormat=application%2Fjson
  format: null
  id: resource_7
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-eurac_cddnutslevel2
spatial:
  bbox:
  - -63.1511917114258
  - -21.3888511657715
  - 55.8357810974121
  - 71.1841659545898
  centroid: null
  countries:
  - ALB
  - AND
  - AUT
  - BEL
  - BGR
  - BIH
  - BLR
  - CHE
  - CYP
  - CZE
  - DEU
  - DNK
  - ESP
  - EST
  - FIN
  - FRA
  - GBR
  - GRC
  - HRV
  - HUN
  - IRL
  - ISL
  - ITA
  - LIE
  - LTU
  - LUX
  - LVA
  - MCO
  - MDA
  - MKD
  - MLT
  - MNE
  - NLD
  - NOR
  - POL
  - PRT
  - ROU
  - RUS
  - SMR
  - SRB
  - SVK
  - SVN
  - SWE
  - UKR
  - VAT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2019'
  start: '2010'
temporal_resolution: null
title: CDD - NUTS level 2
version: null
vulnerability: null
---
