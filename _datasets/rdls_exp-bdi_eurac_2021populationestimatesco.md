---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
creator:
  affiliation: null
  email: kathrin.renner@eurac.edu
  name: Kathrin Renner
  url: https://maps.eurac.edu/api/v2/users/1042
dataset_id: rdls_exp-bdi_eurac_2021populationestimatesco
description: 'Population estimation by UNFPA with Institut de Statistiques et d''Etudes
  Economiques du Burundi (ISTEEBU). Burundi administrative level 0-2 2021 sex and
  age disaggregated projections from 2008 population census statistics [Source: This
  metadata record was automatically extracted from the GeoNode portal eurac]'
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
  description: Population estimates provided by UNFPA using the the Institut de Statistiques
    et d'Etudes Economiques du Burundi 2008 census data. Caveats / Comments The source
    data uses the 129 feature administrative level 2 structure in use in 2008. This
    dataset contains an administrative level 2 table with 129 features and a consolidation
    'bdi_admpop_adm2_2021_119feature' table that corresponds to the structure used
    in the COD-AB. The differences (3 features corresponding to 13 original features)
    are in BUJUMBURA MAIRIE.
  sources:
  - id: source_1
    license: null
    name: Kathrin Renner
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://maps.eurac.edu/catalogue/#/dataset/604
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Kathrin Renner
  url: https://maps.eurac.edu
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (GML 2.0)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=gml2&srs=EPSG%3A32735
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
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (GML 3.1.1)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=text%2Fxml%3B+subtype%3Dgml%2F3.1.1&srs=EPSG%3A32735
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
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (CSV)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=csv&srs=EPSG%3A32735
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
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (Excel)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=excel&srs=EPSG%3A32735
  format: null
  id: resource_3
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
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (JSON)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=json&srs=EPSG%3A32735&srsName=EPSG%3A32735
  format: null
  id: resource_4
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoJSON
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_pop_percommune_2021_isteebu_unfpa_pol_pp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (OGC WMS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:EO_CDR:bdi_pop_percommune_2021_isteebu_unfpa_pol_pp&format=image%2Fpng
  format: null
  id: resource_5
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: EO_CDR Service'
- access_url: https://maps.eurac.edu/datasets/geonode:EO_CDR:bdi_pop_percommune_2021_isteebu_unfpa_pol_pp
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (OGC WFS: EO_CDR Service)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:EO_CDR:bdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=application%2Fjson
  format: null
  id: resource_6
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WFS: EO_CDR Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32735
  description: 'BURUNDI: 2021 Population estimates by Communes (Zipped Shapefile)'
  download_url: https://maps.eurac.edu/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=EO_CDR%3Abdi_pop_percommune_2021_isteebu_unfpa_pol_pp&outputFormat=SHAPE-ZIP&srs=EPSG%3A32735&format_options=charset%3AUTF-8
  format: null
  id: resource_7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Zipped Shapefile
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bdi_eurac_2021populationestimatesco
spatial:
  bbox:
  - 721342.0
  - 9504152.0
  - 929286.375
  - 9745518.0
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: 'BURUNDI: 2021 Population estimates by Communes'
version: null
vulnerability: null
---
