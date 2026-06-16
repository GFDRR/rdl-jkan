---
attributions:
- entity:
    affiliation: null
    email: efehr.hazard@sed.ethz.ch
    name: European Facilities for Earthquake Hazard and Risk (EFEHR)
    url: http://www.efehr.org/start/
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: efehr.hazard@sed.ethz.ch
  name: EFEHR Office
  url: http://www.efehr.org/start/
creator:
  affiliation: null
  email: efehr.hazard@sed.ethz.ch
  name: European Facilities for Earthquake Hazard and Risk (EFEHR)
  url: http://www.efehr.org/start/
dataset_id: rdls_hzd-jrc_drmkc_earthquake
description: Probabilistic modelling of seismic hazard
details: "Probabilistic seismic hazard maps for Europe provide gridded datasets of\
  \ Peak Ground Acceleration (PGA) levels based on comprehensive geological and seismological\
  \ data. The maps express the spatial distribution of ground shaking for specific\
  \ exceedance probabilities (e.g., 10% probability of exceedance in 50 years, corresponding\
  \ to a return period of approximately 475 years). The probabilistic approach considers\
  \ all potential earthquakes that may affect a given location, along with various\
  \ models of seismic wave propagation and ground motion, within a statistical framework.\
  \ The hazard assessments integrate knowledge of past earthquakes, regional geology,\
  \ and tectonic settings to model future earthquake occurrence. Cell values indicate\
  \ PGA levels (typically in m/s\xB2 or g). The maps are used by engineers to derive\
  \ codes for earthquake-resistant construction and by decision-makers to develop\
  \ appropriate measures to reduce earthquake impacts. The dataset is provided by\
  \ EFEHR (European Facilities for Earthquake Hazard and Risk). NOTE: Seismic hazard\
  \ assessments require regular review and updates as new data and scientific knowledge\
  \ become available."
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 20
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: EMS:-
        process: ground_motion
        trigger: null
        type: earthquake
      id: effects_intensity
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_sa
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_pga
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hmap
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: magnitude_radius_probability
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_sa_landing
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_sa_wms
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_sa_ascii
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_sa_discovery
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_pga_landing
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_pga_wms
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_pga_ascii
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hazard_pga_discovery
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hmap_landing
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hmap_wms
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: hmap_shp
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: EMS:-
        process: ground_motion
        trigger: null
        type: earthquake
      id: effects_intensity_landing
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: EMS:-
        process: ground_motion
        trigger: null
        type: earthquake
      id: effects_intensity_wms
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: magnitude_radius_probability_landing
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: EFEHR_Earthquake_Hazard
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: magnitude_radius_probability_wms
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability:
            span: 50
            value: null
          return_period: null
    frequency_distribution: null
    hazards:
    - classification: null
      id: EFEHR_Earthquake_Hazard
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: Earthquake_Hazard
    occurrence_range: 1/10 to 1/10000 years
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Facilities for Earthquake Hazard and Risk (EFEHR)
    risk_data_type: null
    type: model
    url: http://www.efehr.org/start/
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: European Seismic Hazard Model 2020 (ESHM20)
  url: https://hazard.efehr.org/en/web-services/hazard-map-data/
publisher:
  affiliation: null
  email: efehr.hazard@sed.ethz.ch
  name: European Facilities for Earthquake Hazard and Risk (EFEHR)
  url: http://www.efehr.org/
purpose: To support earthquake risk assessment, develop earthquake-resistant construction
  codes, and enable decision-making for seismic risk reduction measures across Europe.
referenced_by:
- author_names:
  - Laurentiu Danciu
  - Shyam Nandan
  - Celso Reyes
  - Roberto Basili
  - Graeme Weatherill
  - Celine Beauval
  - Andrea Rovida
  - Susana Vilanova
  - Karin Sesetyan
  - Pierre-Yves Bard
  - Fabrice Cotton
  - Stefan Wiemer
  - Domenico Giardini
  date_published: '2021-01-01'
  doi: https://doi.org/10.12686/a15
  id: Ref_1
  name: Probabilistic modelling of seismic hazard
  url: https://hazard.efehr.org/en/web-services/hazard-map-data/
resources:
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Parent for layers like effects_intensity{I}plus_{N}yr_{local|solid}.\
    \ Maps show the probability that shaking of EMS-98 intensity \u2265{I} occurs\
    \ at least once within {N} years (PoE in N years). Site class: \u201Clocal\u201D\
    \ = local soil amplification; \u201Csolid\u201D = rock site, typically VS30\u2248\
    600 m/s. Examples: intensity thresholds 4/7/8 and spans 1/50/100 years; derived\
    \ from SUIhaz2015 median."
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&LAYERS=hmap481&VERSION=1.1.1
  format: null
  id: effects_intensity
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: "Effects (EMS-98) \u2013 Intensity exceedance probabilities"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Parent for layers like hazard_{f}hz_{ARP}yr. Maps show spectral acceleration
    (SA) at frequency {f} Hz expected with a specified probability of exceedance over
    an average return period {ARP} years (e.g., 72, 475, 975, 2475, 4975, 10000 yr).
    Frequencies include 0.25, 0.33, 0.5, 1, 1.81, 2.5, 3.33, 4, 5, 6.66, 10, 20 Hz.
    Values correspond to SUIhaz2015 median.
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&LAYERS=hmap481&VERSION=1.1.1
  format: null
  id: hazard_sa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 Spectral Acceleration (SA) at frequency"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Parent for layers like hazard_pga_{ARP}yr. Maps show horizontal peak
    ground acceleration expected with a specified probability of exceedance over an
    average return period {ARP} years (e.g., 72, 475, 975, 2475, 4975, 10000 yr).
    Values correspond to SUIhaz2015 median.
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&LAYERS=hmap481&VERSION=1.1.1
  format: null
  id: hazard_pga
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 Peak Ground Acceleration (PGA)"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Parent for products with IDs hmap####. These are packaged hazard map\
    \ rasters/tiles whose detailed parameters (e.g., PGA vs SA, ARP) are defined in\
    \ the product\u2019s own metadata. Use this parent when referencing the collection\
    \ as a whole; for specifics, consult each hmap item\u2019s metadata. Derived from\
    \ SUIhaz2015 unless otherwise noted."
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&LAYERS=hmap481&VERSION=1.1.1
  format: null
  id: hmap
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 PGA map products (hmap*)"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: "Parent for layers like magnitude_{M}plus_rad{R}km_{N}yr. Maps show\
    \ the probability that at least one earthquake of magnitude \u2265{M} occurs within\
    \ radius {R} km over {N} years (PoE in N years). Typical values include M\u2265\
    2.5/4.5/5/6/7; radii 10/20/30/50 km; spans 1/50/100 years. Based on mean/median\
    \ of SUIhaz2015 as provided."
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&LAYERS=hmap481&VERSION=1.1.1
  format: null
  id: magnitude_radius_probability
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 1000
  temporal: null
  temporal_resolution: null
  title: "Earthquake probability \u2013 Magnitude within radius"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Landing page with WMS and API options for spectral acceleration (SA)
    hazard maps.
  download_url: null
  format: null
  id: hazard_sa_landing
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 SA at frequency \u2013 Access options"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (OGC WMS capabilities for SA
    hazard layers.)
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities
  format: null
  id: hazard_sa_wms
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 SA at frequency \u2013 WMS GetCapabilities"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: ASCII table for a bbox. Provide IMT (e.g., SA[0.50s]), PoE/span, soil,
    aggregation; placeholders must be filled.
  download_url: http://appsrvr.share-eu.org:8080/share/map?id={model_id}&lon1={ll_lon}&lat1={ll_lat}&lon2={ur_lon}&lat2={ur_lat}&imt={IMT}&hmapexceedprob={poe}&hmapexceedyears={years}&soiltype={soiltype}&aggregationtype={aggtype}&aggregationlevel={agglevel}
  format: null
  id: hazard_sa_ascii
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 SA at frequency \u2013 ASCII sub-area API"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Resolve hmapid/hmapwms after
    specifying IMT & PoE/span, soil, and aggregation.)
  download_url: http://appsrvr.share-eu.org:8080/share/model?id={model_id}&imt={IMT}&hmapexceedprob={poe}&hmapexceedyears={years}&soiltype={soiltype}&aggregationtype={aggtype}&aggregationlevel={agglevel}
  format: null
  id: hazard_sa_discovery
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 SA at frequency \u2013 Model/Layer discovery"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Landing page with WMS and API
    options for PGA hazard maps.)
  download_url: null
  format: null
  id: hazard_pga_landing
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 PGA \u2013 Access options"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (OGC WMS capabilities for PGA
    hazard layers.)
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities
  format: null
  id: hazard_pga_wms
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 PGA \u2013 WMS GetCapabilities"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: ASCII table for a bbox. IMT=PGA plus PoE/span, soil, aggregation; placeholders
    must be filled.
  download_url: http://appsrvr.share-eu.org:8080/share/map?id={model_id}&lon1={ll_lon}&lat1={ll_lat}&lon2={ur_lon}&lat2={ur_lat}&imt=PGA&hmapexceedprob={poe}&hmapexceedyears={years}&soiltype={soiltype}&aggregationtype={aggtype}&aggregationlevel={agglevel}
  format: null
  id: hazard_pga_ascii
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 PGA \u2013 ASCII sub-area API"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Resolve hmapid/hmapwms for
    PGA after specifying PoE/span, soil, and aggregation.)
  download_url: http://appsrvr.share-eu.org:8080/share/model?id={model_id}&imt=PGA&hmapexceedprob={poe}&hmapexceedyears={years}&soiltype={soiltype}&aggregationtype={aggtype}&aggregationlevel={agglevel}
  format: null
  id: hazard_pga_discovery
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 PGA \u2013 Model/Layer discovery"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Landing page with WMS preview
    and packaged SHP downloads for hmap#### products.)
  download_url: null
  format: null
  id: hmap_landing
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 hmap* packaged products \u2013 Access options"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (OGC WMS capabilities (use LAYERS=hmap{hmapid}
    with GetMap).)
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities
  format: null
  id: hmap_wms
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 hmap* \u2013 WMS GetCapabilities"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Direct packaged download as ESRI Shapefile ZIP. Replace {hmapid} (only
    files named hmap####.zip are available).
  download_url: http://efehrappsrvr.ethz.ch/share/staticdownload/hmap{hmapid}.zip
  format: null
  id: hmap_shp
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Hazard \u2013 hmap* \u2013 SHP download (ZIP)"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Landing page for EMS-98 intensity
    exceedance maps (local vs rock sites).)
  download_url: null
  format: null
  id: effects_intensity_landing
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Effects (EMS-98) \u2013 Access options"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (OGC WMS capabilities listing
    EMS-98 layers (preview/visualize).)
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities
  format: null
  id: effects_intensity_wms
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Effects (EMS-98) \u2013 WMS GetCapabilities"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (Landing page for magnitude-within-radius
    probability maps.)
  download_url: null
  format: null
  id: magnitude_radius_probability_landing
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Earthquake probability \u2013 Magnitude within radius \u2013 Access options"
- access_url: https://hazard.efehr.org/en/web-services/hazard-map-data/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: EFEHR Earthquakes Hazard Map of Europe (OGC WMS capabilities listing
    magnitude-in-radius layers (preview/visualize).)
  download_url: http://efehrmaps.ethz.ch/cgi-bin/mapserv?MAP=/var/www/mapfile/sharehazard.01.map&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities
  format: null
  id: magnitude_radius_probability_wms
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: "Earthquake probability \u2013 Magnitude within radius \u2013 WMS GetCapabilities"
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_earthquake
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: EFEHR Earthquakes Hazard Map of Europe
version: '1'
vulnerability: null
---
